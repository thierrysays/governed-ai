# governed-ai. Run `make help`. Requires Python 3.11+ and the `opa` binary for policy tests.

PY     ?= python3
VENV   ?= .venv
BIN    := $(VENV)/bin
PYTHON := $(BIN)/python
OPA    ?= opa

.DEFAULT_GOAL := help
.PHONY: help setup validate test test-py test-policies check clean

help: ## List targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk -F':.*?## ' '{printf "  %-16s %s\n", $$1, $$2}'

$(PYTHON):
	$(PY) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt

setup: $(PYTHON) ## Create the virtualenv and install pinned dependencies

validate: $(PYTHON) ## Validate registry/*.yaml
	$(PYTHON) tools/validate_registry.py

test-py: $(PYTHON) ## Python tests (registry validator, negative tests)
	$(PYTHON) -m pytest -q tests

test-policies: ## Rego format check, strict compile and tests (needs opa)
	@command -v $(OPA) >/dev/null || { echo "opa not found: install it or set OPA=/path/to/opa"; exit 1; }
	$(OPA) fmt --fail policies
	$(OPA) check --strict policies
	$(OPA) test policies -v

test: test-py test-policies ## All tests

check: validate test ## What CI runs

clean: ## Remove the virtualenv and caches
	rm -rf $(VENV) .pytest_cache
