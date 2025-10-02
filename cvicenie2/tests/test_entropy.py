"""
Tests for entropy calculations.
"""
import sys
from pathlib import Path
import math

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

# Try importing pytest, fallback to manual test runner
try:
    import pytest
    HAS_PYTEST = True
except ImportError:
    HAS_PYTEST = False

from entropy import entropy_equiprobable


def test_entropy_power_of_2():
    """Test entropy for perfect powers of 2."""
    assert entropy_equiprobable(2) == 1.0
    assert entropy_equiprobable(4) == 2.0
    assert entropy_equiprobable(8) == 3.0
    assert entropy_equiprobable(16) == 4.0
    assert entropy_equiprobable(32) == 5.0
    assert entropy_equiprobable(64) == 6.0
    assert entropy_equiprobable(128) == 7.0
    assert entropy_equiprobable(256) == 8.0


def test_entropy_required_values():
    """Test required entropy values from specification."""
    h8 = entropy_equiprobable(8)
    h128 = entropy_equiprobable(128)
    
    assert h8 == 3.0, f"H(8) should be 3, got {h8}"
    assert h128 == 7.0, f"H(128) should be 7, got {h128}"


def test_entropy_non_power_of_2():
    """Test entropy for non-powers of 2."""
    # H(10) = log2(10) ≈ 3.321928
    h10 = entropy_equiprobable(10)
    assert abs(h10 - 3.321928) < 0.00001
    
    # H(100) = log2(100) ≈ 6.643856
    h100 = entropy_equiprobable(100)
    assert abs(h100 - 6.643856) < 0.00001


def test_entropy_properties():
    """Test mathematical properties of entropy."""
    # H(n*m) = H(n) + H(m) for equiprobable distributions
    h2 = entropy_equiprobable(2)
    h4 = entropy_equiprobable(4)
    h8 = entropy_equiprobable(8)
    
    assert abs(h4 - (h2 + h2)) < 0.00001
    assert abs(h8 - (h4 + h2)) < 0.00001


def test_entropy_comparison():
    """Test that entropy increases with number of outcomes."""
    h2 = entropy_equiprobable(2)
    h8 = entropy_equiprobable(8)
    h128 = entropy_equiprobable(128)
    
    assert h2 < h8 < h128


def test_entropy_errors():
    """Test error handling."""
    try:
        entropy_equiprobable(0)
        assert False, "Should raise ValueError for n=0"
    except ValueError as e:
        assert "positive" in str(e)
    
    try:
        entropy_equiprobable(-5)
        assert False, "Should raise ValueError for negative n"
    except ValueError as e:
        assert "positive" in str(e)


def test_entropy_formula():
    """Verify that H(n) = log2(n)."""
    for n in [2, 5, 8, 10, 16, 100, 128, 1000]:
        expected = math.log2(n)
        actual = entropy_equiprobable(n)
        assert abs(actual - expected) < 0.0000001, f"H({n}) mismatch"


# Manual test runner for environments without pytest
def run_tests_manually():
    """Run all tests manually without pytest."""
    test_functions = [
        test_entropy_power_of_2,
        test_entropy_required_values,
        test_entropy_non_power_of_2,
        test_entropy_properties,
        test_entropy_comparison,
        test_entropy_errors,
        test_entropy_formula,
    ]
    
    print("Running entropy tests manually...\n")
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
