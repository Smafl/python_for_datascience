PYTHON_VERSION := 3.10
PYTHON_BIN := python$(PYTHON_VERSION)

check_python:
	@echo "Checking for Python $(PYTHON_VERSION)..."
	@if command -v $(PYTHON_BIN) >/dev/null 2>&1; then \
		echo "$(PYTHON_BIN) is installed."; \
	else \
		echo "$(PYTHON_BIN) not found. Installing..."; \
		if command -v apt-get >/dev/null 2>&1; then \
			sudo apt-get update && sudo apt-get install -y python$(PYTHON_VERSION); \
		elif command -v dnf >/dev/null 2>&1; then \
			sudo dnf install -y python$(PYTHON_VERSION); \
		elif command -v brew >/dev/null 2>&1; then \
			brew install python@$(PYTHON_VERSION); \
		else \
			echo "No supported package manager found. Please install Python $(PYTHON_VERSION) manually."; \
			exit 1; \
		fi \
	fi

.PHONY: check_python
