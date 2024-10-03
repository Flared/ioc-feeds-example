.PHONY: lint
lint: venv mypy format-check

.PHONY: format
format: venv
	venv/bin/ruff check --fix
	venv/bin/ruff format

.PHONY: format-check
format-check: venv
	venv/bin/ruff format --check

.PHONY: mypy
mypy:
	venv/bin/mypy *.py

venv: requirements.txt
	rm -rf venv
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

.PHONY: clean
clean:
	rm -rf venv
