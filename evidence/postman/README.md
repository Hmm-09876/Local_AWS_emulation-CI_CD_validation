# Postman Evidence
This folder has Postman files used for quick API checks. It keeps the collection, environment, and short run notes.

Files:

- `api smoke tests.postman_collection.json` — collection with basic requests (`GET /`, `GET /health`, `GET /no-such-route`).
- `demo-3.postman_environment.json` — variables for local runs (e.g., `base_url = http://localhost:8080`).
- `run-notes.md` — short notes about each run (URL, which requests, results).

Quick run (use npx to avoid global install):

```bash
npx newman run "evidence/postman/api smoke tests.postman_collection.json" -e "evidence/postman/demo-3.postman_environment.json"
```

Expected smoke results:

- `GET /` → 200, body contains `status: ok`
- `GET /health` → 200, body contains `status: ok`
- `GET /no-such-route` → 404

Goal: keep a small, easy check to confirm the app is running and basic routes work.
