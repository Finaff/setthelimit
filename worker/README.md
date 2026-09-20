# Set the Limit — API worker

One Cloudflare Worker with a D1 database. It stores anonymous runs for the crowd layer, signs
people in with X, lets anyone attach their run to their X handle (opt-in), and lets a listed
public figure replace our predictions with their own answers. Endpoints are listed at the top
of `src/index.js`. Nothing personal is stored for anonymous runs: coordinates, the encoded
answers, a language code and a daily-salted hash of the address used only for rate limiting.

## Set up once (after setthelimit.com exists)

1. `npm i -g wrangler` (or use `npx wrangler`), `wrangler login`.
2. `wrangler d1 create setthelimit` → paste the id into `wrangler.toml`.
3. `wrangler d1 execute setthelimit --remote --file schema.sql`.
4. X developer portal → create an app with OAuth 2.0, type *Web App* (confidential client),
   callback `https://api.setthelimit.com/auth/x/callback`, website `https://setthelimit.com`,
   scopes `users.read tweet.read`. Put the client id in `wrangler.toml`; then
   `wrangler secret put X_CLIENT_SECRET` and `wrangler secret put SESSION_SECRET` (any long random string).
5. Fill `FIGURE_ACCOUNTS` with `{"<numeric X user id>": "<figure id>"}` from
   `research/x-accounts.json` once the ids are verified against the X API (`GET /2/users/by/username/:handle`).
   Match on the numeric id, never on the handle.
6. `wrangler deploy`. In DNS, `api.setthelimit.com` is created by the custom-domain route.
7. In `site/index.html`, set `window.STL_API = 'https://api.setthelimit.com'`.

## Local run

`wrangler dev --local` with `DEV = "1"` in a `.dev.vars` file allows `http://localhost:8766` as origin;
apply `schema.sql` with `wrangler d1 execute setthelimit --local --file schema.sql`.
