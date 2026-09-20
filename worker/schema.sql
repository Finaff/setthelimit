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
-- Comments on a proposition: X sign-in required (keeps bots out). One level of replies. `value` is the author's own answer, if they chose to show it.
CREATE TABLE IF NOT EXISTS comments (
  id TEXT PRIMARY KEY, item_id TEXT NOT NULL, parent_id TEXT, x_user_id TEXT NOT NULL, handle TEXT NOT NULL, name TEXT,
  body TEXT NOT NULL, value INTEGER, lang TEXT, at TEXT NOT NULL, deleted INTEGER NOT NULL DEFAULT 0);
CREATE INDEX IF NOT EXISTS comments_item ON comments(item_id, at);
CREATE INDEX IF NOT EXISTS comments_user ON comments(x_user_id, at);
CREATE TABLE IF NOT EXISTS comment_votes (comment_id TEXT NOT NULL, x_user_id TEXT NOT NULL, at TEXT NOT NULL, PRIMARY KEY (comment_id, x_user_id));
CREATE TABLE IF NOT EXISTS comment_flags (comment_id TEXT NOT NULL, x_user_id TEXT NOT NULL, at TEXT NOT NULL, PRIMARY KEY (comment_id, x_user_id));
-- X accounts that have signed in (numeric id, current handle, display name): needed to name moderators and verified figures by id.
CREATE TABLE IF NOT EXISTS accounts (x_user_id TEXT PRIMARY KEY, handle TEXT NOT NULL, name TEXT, first_at TEXT NOT NULL, last_at TEXT NOT NULL);
