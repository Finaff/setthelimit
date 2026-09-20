-- Anonymous runs: coordinates, the encoded answers (same ?r= format as the share link), nothing else.
CREATE TABLE IF NOT EXISTS runs (
  id TEXT PRIMARY KEY, x REAL NOT NULL, y REAL NOT NULL, r TEXT NOT NULL, v TEXT, lang TEXT,
  at TEXT NOT NULL, ip_hash TEXT, token_hash TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS runs_at ON runs(at);
CREATE INDEX IF NOT EXISTS runs_ip ON runs(ip_hash, at);
-- Opt-in: a run attached to an X handle by its owner. One per X account; deleting is one call.
CREATE TABLE IF NOT EXISTS public_results (
  x_user_id TEXT PRIMARY KEY, handle TEXT NOT NULL, name TEXT, run_id TEXT NOT NULL, at TEXT NOT NULL);
-- A listed figure's own answers, replacing our predictions. Revoked rows are kept for the record.
CREATE TABLE IF NOT EXISTS claims (
  figure_id TEXT PRIMARY KEY, x_user_id TEXT NOT NULL, handle TEXT NOT NULL, name TEXT,
  r TEXT NOT NULL, at TEXT NOT NULL, revoked INTEGER NOT NULL DEFAULT 0);
