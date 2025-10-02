"""
Tests for XOR utilities.
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

# Try importing pytest, fallback to manual test runner
try:
    import pytest
    HAS_PYTEST = True
except ImportError:
    HAS_PYTEST = False

from xor_utils import xor_chain, evaluate_expression


def test_xor_chain_two():
    """Test XOR with two bitstrings."""
    assert xor_chain("1011", "0110") == "1101"
    assert xor_chain("1111", "0000") == "1111"
    assert xor_chain("1010", "1010") == "0000"


def test_xor_chain_three():
    """Test XOR with three bitstrings."""
    assert xor_chain("1011", "0110", "0100") == "1001"
    assert xor_chain("0101", "1110", "1101") == "0110"


def test_xor_chain_properties():
    """Test XOR properties."""
    # Commutative: a ⊕ b = b ⊕ a
    assert xor_chain("1011", "0110") == xor_chain("0110", "1011")
    
    # Associative: (a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)
    a, b, c = "1011", "0110", "0100"
    assert xor_chain(a, b, c) == xor_chain(xor_chain(a, b), c)
    
    # Identity: a ⊕ 0 = a
    assert xor_chain("1011", "0000") == "1011"
    
    # Self-inverse: a ⊕ a = 0
    assert xor_chain("1011", "1011") == "0000"


def test_evaluate_expression_testset1():
    """Test expression evaluation with test set 1."""
    a, b, c = "1011", "0110", "0100"
    result = evaluate_expression(a, b, c)
    assert result == "0100", f"Expected 0100, got {result}"


def test_evaluate_expression_testset2():
    """Test expression evaluation with test set 2."""
    a, b, c = "0101", "1110", "1101"
    result = evaluate_expression(a, b, c)
    assert result == "1101", f"Expected 1101, got {result}"


def test_evaluate_expression_equals_c():
    """Test that a⊕b⊕c⊕a⊕b always equals c."""
    # Mathematical proof: a⊕b⊕c⊕a⊕b = (a⊕a)⊕(b⊕b)⊕c = 0⊕0⊕c = c
    test_cases = [
        ("1011", "0110", "0100"),
        ("0101", "1110", "1101"),
        ("1111", "0000", "1010"),
        ("0000", "1111", "0101"),
    ]
    
    for a, b, c in test_cases:
        result = evaluate_expression(a, b, c)
        assert result == c, f"Expected {c}, got {result} for a={a}, b={b}, c={c}"


def test_xor_chain_errors():
    """Test error handling."""
    # Different lengths
    try:
        xor_chain("101", "0110")
        assert False, "Should raise ValueError for different lengths"
    except ValueError as e:
        assert "same length" in str(e)
    
    # Invalid characters
    try:
        xor_chain("1021", "0110")
        assert False, "Should raise ValueError for invalid characters"
    except ValueError as e:
        assert "only '0' and '1'" in str(e)
    
    # No arguments
    try:
        xor_chain()
        assert False, "Should raise ValueError for no arguments"
    except ValueError as e:
        assert "at least one" in str(e).lower()


# Manual test runner for environments without pytest
def run_tests_manually():
    """Run all tests manually without pytest."""
    test_functions = [
        test_xor_chain_two,
        test_xor_chain_three,
        test_xor_chain_properties,
        test_evaluate_expression_testset1,
        test_evaluate_expression_testset2,
        test_evaluate_expression_equals_c,
        test_xor_chain_errors,
    ]
    
    print("Running XOR tests manually...\n")
    passed = 0
    failed = 0
    
    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ {test_func.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"✗ {test_func.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__}: Unexpected error: {e}")
            failed += 1
    
    print(f"\n{passed} passed, {failed} failed")
    return failed == 0


if __name__ == '__main__':
    if not HAS_PYTEST:
        success = run_tests_manually()
        sys.exit(0 if success else 1)
    else:
        # Run with pytest
        sys.exit(pytest.main([__file__, '-v']))
