"""
Tests for Polybius square encoding/decoding.
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

from polybius import encode, decode, normalize_text, remove_diacritics


def test_remove_diacritics():
    """Test diacritics removal."""
    assert remove_diacritics("BEDNÁR") == "BEDNAR"
    assert remove_diacritics("Ľuboš") == "Lubos"
    assert remove_diacritics("ČĎŤŇŠŽÝÁÍÉ") == "CDTNSZYAIE"


def test_normalize_text():
    """Test text normalization."""
    assert normalize_text("bednár") == "BEDNAR"
    assert normalize_text("Encrypt Me") == "ENCRYPT ME"


def test_encode_basic():
    """Test basic Polybius encoding."""
    pairs, concat = encode("A")
    assert pairs == "11"
    assert concat == "11"
    
    pairs, concat = encode("ABC")
    assert pairs == "11 12 13"
    assert concat == "111213"


def test_encode_with_spaces():
    """Test encoding with spaces preserved."""
    pairs, concat = encode("A B")
    assert pairs == "11  12"
    assert concat == "11 12"


def test_encode_acceptance_test():
    """Test acceptance case: ENCRYPT ME 2 DAY"""
    pairs, concat = encode("ENCRYPT ME 2 DAY")
    assert pairs == "15 32 13 36 51 34 42  31 15  55  14 11 51"
    assert concat == "15321336513442 3115 55 141151"


def test_encode_surname():
    """Test encoding surname BEDNÁR."""
    pairs, concat = encode("BEDNÁR")
    # BEDNÁR -> BEDNAR -> 12 15 14 32 11 36
    assert pairs == "12 15 14 32 11 36"
    assert concat == "121514321136"


def test_decode_basic():
    """Test basic Polybius decoding."""
    assert decode("11") == "A"
    assert decode("11 12 13") == "ABC"


def test_decode_with_spaces():
    """Test decoding with spaces."""
    decoded = decode("11  12")
    assert decoded.strip() == "A B"


def test_decode_acceptance_test():
    """Test decoding acceptance case."""
    decoded = decode("15 32 13 36 51 34 42  31 15  55  14 11 51")
    # Should decode to "ENCRYPT ME 2 DAY"
    cleaned = ' '.join(decoded.split())  # Normalize spaces
    assert cleaned == "ENCRYPT ME 2 DAY"


def test_roundtrip():
    """Test encoding then decoding returns original."""
    original = "HELLO WORLD 123"
    pairs, _ = encode(original)
    decoded = decode(pairs)
    # Normalize spaces for comparison
    assert ' '.join(decoded.split()) == original


def test_roundtrip_surname():
    """Test surname roundtrip."""
    original = "BEDNÁR"
    pairs, _ = encode(original)
    decoded = decode(pairs)
    assert decoded == "BEDNAR"  # Diacritics removed


def test_all_characters():
    """Test that all characters in the grid work."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    pairs, concat = encode(alphabet)
    decoded = decode(pairs)
    assert decoded == alphabet


# Manual test runner for environments without pytest
def run_tests_manually():
    """Run all tests manually without pytest."""
    test_functions = [
        test_remove_diacritics,
        test_normalize_text,
        test_encode_basic,
        test_encode_with_spaces,
        test_encode_acceptance_test,
        test_encode_surname,
        test_decode_basic,
        test_decode_with_spaces,
        test_decode_acceptance_test,
        test_roundtrip,
        test_roundtrip_surname,
        test_all_characters,
    ]
    
    print("Running Polybius tests manually...\n")
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
