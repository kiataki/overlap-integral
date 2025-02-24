# Define variables
PYTHON = python
POETRY = poetry

# Default target
all: test

# Run tests
test:
	$(POETRY) run $(PYTHON) tests/test_overlap_integral.py

# Help command
help:
	@echo "Makefile commands:"
	@echo "  all            - Run the tests"
	@echo "  test           - Run the tests in tests/test_overlap_integral.py"
	@echo "  help           - Show this help message"
