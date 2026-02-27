# Sample QA pytest project (for Copilot Agent Mode exercises)

## Setup
```bash
python -m venv .venv
# activate venv (platform-specific)
python -m pip install -r requirements-dev.txt
pytest
```

## Exercises mapping
- Exercise 1 (refactor one test file): `tests/test_calculator_messy.py`
- Exercise 2 (add logs across multiple files): `tests/test_auth_flaky.py`, `tests/test_integration_workflow.py`
- Exercise 3 (fix failing test + commit): `tests/test_auth_flaky.py::test_login_token_is_stable_for_same_credentials`