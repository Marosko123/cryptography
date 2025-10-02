# Variables
PYTHON = python3
SRC_DIR = src
TEST_DIR = tests
SURNAME = BEDNAR

# Default target
.PHONY: all
all: test

# Run Atbash cipher (stream mode)
.PHONY: run-stream
run-stream:
	@echo "Running Atbash cipher with surname: $(SURNAME)"
	$(PYTHON) $(SRC_DIR)/cipher.py --surname "$(SURNAME)" --mode stream

# Run block cipher
.PHONY: run-block
run-block:
	@echo "Running block cipher with surname: $(SURNAME)"
	$(PYTHON) $(SRC_DIR)/cipher.py --surname "$(SURNAME)" --mode block

# Run both modes for benchmarking
.PHONY: bench
bench:
	@echo "=== PERFORMANCE BENCHMARK ==="
	@echo "Testing with surname: $(SURNAME)"
	@echo ""
	@echo "--- ATBASH CIPHER ---"
	$(PYTHON) $(SRC_DIR)/cipher.py --surname "$(SURNAME)" --mode stream
	@echo ""
	@echo "--- BLOCK CIPHER ---"
	$(PYTHON) $(SRC_DIR)/cipher.py --surname "$(SURNAME)" --mode block
	@echo ""
	@echo "=== BENCHMARK COMPLETE ==="

# Run tests
.PHONY: test
test:
	@echo "Running unit tests..."
	$(PYTHON) -m pytest $(TEST_DIR)/ -v

# Format code with ruff (if available) or use basic formatting
.PHONY: format
format:
	@echo "Formatting code..."
	@if command -v ruff >/dev/null 2>&1; then \
		ruff format $(SRC_DIR)/ $(TEST_DIR)/; \
		echo "Code formatted with ruff"; \
	else \
		echo "ruff not available, skipping formatting"; \
		echo "Install ruff with: pip install ruff"; \
	fi

# Clean up Python cache files
.PHONY: clean
clean:
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

# Run example with different surname
.PHONY: demo
demo:
	@echo "Demo with surname 'SMITH':"
	$(PYTHON) $(SRC_DIR)/cipher.py --surname "SMITH" --mode stream
	@echo ""
	@echo "Demo with surname 'SMITH' (block):"
	$(PYTHON) $(SRC_DIR)/cipher.py --surname "SMITH" --mode block

# Show help
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  run-stream  - Run Atbash cipher with default surname"
	@echo "  run-block   - Run block cipher with default surname" 
	@echo "  bench       - Run performance benchmark for both modes"
	@echo "  test        - Run unit tests"
	@echo "  format      - Format code (requires ruff)"
	@echo "  clean       - Remove Python cache files"
	@echo "  demo        - Run examples with 'SMITH'"
	@echo "  help        - Show this help message"
	@echo ""
	@echo "Override surname: make run-stream SURNAME=YOURNAME"