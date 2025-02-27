# Define variables
PYTHON = python
POETRY = poetry
PYTEST = pytest

# Default target
all: test

# Run tests
personal_test:
	$(POETRY) run $(PYTHON) tests/personal_test_overlap_integral.py

test:
	$(PYTEST) tests/test_overlap_integral.py

# Help command
help:
	@echo "Makefile commands:"
	@echo "  all            - Run the tests"
	@echo "  personal_test  - Run the tests in tests/personal_test_overlap_integral.py"
	@echo "  test         - Run the tests in tests/test_overlap_integral.py"
	@echo "  help           - Show this help message"
