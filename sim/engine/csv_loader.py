#!/usr/bin/env python3
"""Mode-P CSV loader — the provisional-dataset ingestion path.

NON-FORMAL — SIMULATION TRIAL — MODE P — PROVISIONAL DATA PATH.

Converts a two-column CSV into the observation schedule the already-validated
engine consumes. It performs NO market-data cleaning, NO gap filling, NO
interpolation, NO adjustment and NO reordering: it validates and normalizes, or
it fails closed.

Deliberately NOT a market-data framework. There is no vendor abstraction, no
OHLC, no volume, no FX, no corporate actions. Those would be architecture for
hypothetical futures; this is the narrowest contract that lets one acceptable
historical CSV reach the engine.
"""
from decimal import Decimal
from datetime import date
from pathlib import Path
import csv, hashlib, io

from engine import FixtureError

# The minimum contract. Header matching is case-insensitive and
# whitespace-insensitive; nothing else about the file is negotiable.
DATE_ALIASES = ("date", "observation_date", "obs_date")
CLOSE_ALIASES = ("close", "value", "index", "index_level", "level", "price", "closing_level")


class CsvContractError(FixtureError):
    """Raised INSTEAD of loading whenever the input would produce meaningless
    engine state. Subclasses FixtureError so existing fail-closed handling and
    the Mode-E guard tests apply unchanged."""


def _norm(s):
    return (s or "").strip().strip("﻿").lower().replace(" ", "_")


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_csv_observations(path, extra_columns="reject"):
    """Read `path` and return (observations, meta).

    observations: [{"date": "YYYY-MM-DD", "close": "<decimal string>"}, ...]
    meta: ingestion facts for the manifest — never economic quantities.

    `extra_columns` policy, explicit by requirement rather than implicit:
      "reject" (default) — any unexpected column is a hard failure. Chosen as the
                           default because an unrecognised column in a real
                           provisional dataset usually means the file is not the
                           file we think it is.
      "ignore"           — unexpected columns are dropped, and their names are
                           recorded in meta so the choice is visible in evidence.
    """
    p = Path(path)
    if not p.exists():
        raise CsvContractError(f"input file does not exist: {p}")

    raw = p.read_bytes()
    if not raw.strip():
        raise CsvContractError("empty file: no header, no observations")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as e:
        raise CsvContractError(f"input is not valid UTF-8: {e}")

    reader = csv.reader(io.StringIO(text))
    try:
        header = next(reader)
    except StopIteration:
        raise CsvContractError("empty file: no header row")

    cols = [_norm(h) for h in header]
    date_idx = next((i for i, c in enumerate(cols) if c in DATE_ALIASES), None)
    close_idx = next((i for i, c in enumerate(cols) if c in CLOSE_ALIASES), None)
    if date_idx is None:
        raise CsvContractError(
            f"required date column not found; accepted names {DATE_ALIASES}, saw {cols}")
    if close_idx is None:
        raise CsvContractError(
            f"required close column not found; accepted names {CLOSE_ALIASES}, saw {cols}")
    if date_idx == close_idx:
        raise CsvContractError("date and close resolved to the same column")

    extras = [c for i, c in enumerate(cols) if i not in (date_idx, close_idx) and c != ""]
    if extras and extra_columns == "reject":
        raise CsvContractError(
            f"unexpected column(s) {extras}; pass extra_columns='ignore' to accept them")
    if extra_columns not in ("reject", "ignore"):
        raise CsvContractError(f"unknown extra_columns policy {extra_columns!r}")

    obs, seen, prev = [], set(), None
    for lineno, row in enumerate(reader, start=2):
        if not row or all(not (c or "").strip() for c in row):
            continue                                   # wholly blank line
        if len(row) <= max(date_idx, close_idx):
            raise CsvContractError(f"line {lineno}: short row, {len(row)} field(s)")

        ds, cs = (row[date_idx] or "").strip(), (row[close_idx] or "").strip()
        if ds == "":
            raise CsvContractError(f"line {lineno}: blank date")
        if cs == "":
            raise CsvContractError(f"line {lineno}: blank close for {ds}")
        try:
            d = date.fromisoformat(ds)
        except ValueError:
            raise CsvContractError(f"line {lineno}: malformed date {ds!r} (expected YYYY-MM-DD)")
        try:
            c = Decimal(cs)
        except Exception:
            raise CsvContractError(f"line {lineno} ({ds}): malformed numeric close {cs!r}")
        if not c.is_finite():
            raise CsvContractError(f"line {lineno} ({ds}): non-finite close {cs!r}")
        if c <= 0:
            raise CsvContractError(
                f"line {lineno} ({ds}): non-positive close {cs!r}; the engine's drawdown "
                f"mechanics require a positive reference high")
        if d in seen:
            raise CsvContractError(f"line {lineno}: duplicate observation date {d}")
        if prev is not None and d <= prev:
            raise CsvContractError(
                f"line {lineno}: dates must be strictly increasing; {d} follows {prev}. "
                f"The loader NEVER reorders input.")
        seen.add(d)
        prev = d
        # `cs` is preserved verbatim, not re-rendered from Decimal, so the engine
        # sees exactly the digits the publisher supplied.
        obs.append({"date": d.isoformat(), "close": cs})

    if not obs:
        raise CsvContractError("no observations after the header row")
    if len(obs) < 2:
        raise CsvContractError(
            f"only {len(obs)} observation(s); MP-R-02 executes at the NEXT observation, "
            f"so at least 2 are required for any execution to be possible")

    meta = {
        "input_filename": p.name,
        "input_sha256": sha256_file(p),
        "input_bytes": len(raw),
        "observation_count": len(obs),
        "first_observation": obs[0]["date"],
        "last_observation": obs[-1]["date"],
        "date_column": cols[date_idx],
        "close_column": cols[close_idx],
        "extra_columns_policy": extra_columns,
        "extra_columns_seen": extras,
    }
    return obs, meta


def build_fixture(csv_path, parameters, dataset_id, extra_columns="reject"):
    """Assemble the in-memory fixture the engine already accepts. The engine is
    reused unchanged — no Mode-P strategy code exists anywhere."""
    obs, meta = load_csv_observations(csv_path, extra_columns=extra_columns)
    return {
        "fixture_id": dataset_id,
        "scenario_name": f"Mode-P provisional dataset {dataset_id}",
        "parameters": parameters,
        "observations": obs,
    }, meta
