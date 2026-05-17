# Flix App — Agent Notes

## Stack

- Python 3.14 + Streamlit (frontend & server in one)
- `uv` for package management (`uv.lock`, `pyproject.toml`)
- External REST API at `http://localhost:8000/api/v1/` (local Flix_API) — JWT auth required
- `streamlit-aggrid` for data tables, `plotly` for charts

## Commands

```bash
uv run streamlit run app.py       # start the app
uv run flake8 .                    # lint (ignores E501, excludes .venv)
uv sync                            # install/sync deps
```

No test suite, no type checker, no CI.

## Architecture

3-layer pattern per feature module — every domain directory follows this:

```
<module>/
  page.py     → Streamlit UI (function named show_<module>)
  service.py  → Business logic (class <Module>Service)
  repository.py → HTTP calls to external API (class <Module>Repository)
```

**Exception:** `movies/` uses `services.py` (plural) instead of `service.py`.

**Exception:** `api/` has only `service.py` (Auth class, no page or repository).

**Exception:** `login/` has `page.py` + `service.py` (functions, not class-based).

**Exception:** `reviews/` lacks `repository.py` and `service.py` for create — `page.py` imports `ReviewService` directly but repository layer is incomplete.

Entry point: `app.py` — checks `st.session_state.token`, routes to login or sidebar menu.

## Key Conventions

- Page functions must be named `show_<module>()` (e.g. `show_genres`, `show_actors`)
- Service classes follow `<Module>Service` pattern
- Repository classes follow `<Module>Repository` pattern
- Private attributes use double-underscore prefix (`self.__base_url`)
- Data normalization: always `pd.json_normalize()` before AgGrid
- Auth token stored in `st.session_state.token`; 401 responses trigger `logout()` from `login.service`
- All API calls use `requests` library with Bearer token in headers

## Gotchas

- `movies/services.py` is plural — importing as `movies.service` will fail
- `reviews/page.py` has a typo: variable named `revies_service` (should be `reviews_service`)
- No local database — all data comes from the external API; the app won't work offline
- `main.py` is a leftover hello-world stub; the real entry point is `app.py`
- `config.toml` only has `app_title` — not used by the app code currently