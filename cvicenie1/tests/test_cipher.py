"""
Unit tests for cipher implementation.
"""
try:
    import pytest
    HAS_PYTEST = True
except ImportError:
    HAS_PYTEST = False
    # Mock pytest decorators when pytest is not available
    class MockMark:
        @staticmethod
        def parametrize(param_name, values):
            def decorator(func):
                # Store test cases on function for manual execution
                func._test_cases = values
                return func
            return decorator
    
    class MockPytest:
        mark = MockMark()
        
        @staticmethod
        def main(args):
            print("pytest not available, skipping automated test run")
    
    pytest = MockPytest()
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.cipher import CipherProcessor
from src.mappings import (
    build_atbash_mapping,
    build_block_mapping,
    get_direct_numbers,
    get_reverse_numbers,
    format_mapping_table,
    get_part_tables,
)


class TestMappings:
    """Test mapping functions."""
    
    def test_atbash_mapping(self):
        """Test Atbash mapping construction."""
        mapping = build_atbash_mapping()
        assert mapping['A'] == 'Z'
        assert mapping['Z'] == 'A'
        assert mapping['M'] == 'N'
        assert mapping['N'] == 'M'
        assert len(mapping) == 26
    
    def test_block_mapping_default(self):
        """Test default block mapping."""
        mapping = build_block_mapping()
        # Part 1: A-M
        assert mapping['A'] == 'M'
        assert mapping['M'] == 'A'
        assert mapping['G'] == 'G'  # Middle of part 1 (7th position both ways)
        # Part 2: N-Z
        assert mapping['N'] == 'Z'
        assert mapping['Z'] == 'N'
        assert mapping['S'] == 'U'  # S->U in reversed part 2
    
    def test_block_mapping_custom(self):
        """Test custom block mapping."""
        part1 = "ABCDE"
        part2 = "FGHIJ"
        mapping = build_block_mapping(part1, part2)
        assert mapping['A'] == 'E'
        assert mapping['B'] == 'D'
        assert mapping['F'] == 'J'
        assert mapping['G'] == 'I'
    
    def test_direct_numbers(self):
        """Test direct numbering."""
        numbers = get_direct_numbers("AZ")
        assert numbers == [1, 26]
        
        numbers = get_direct_numbers("HELLO")
        assert numbers == [8, 5, 12, 12, 15]
    
    def test_reverse_numbers(self):
        """Test reverse numbering."""
        numbers = get_reverse_numbers("AZ")
        assert numbers == [26, 1]
        
        numbers = get_reverse_numbers("HELLO")
        assert numbers == [19, 22, 15, 15, 12]


class TestCipherProcessor:
    """Test cipher processor."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.processor = CipherProcessor()
    
    def test_normalize_input(self):
        """Test input normalization."""
        assert self.processor.normalize_input("hello world!") == "HELLOWORLD"
        assert self.processor.normalize_input("Test123") == "TEST"
        assert self.processor.normalize_input("") == ""
    
    def test_apply_cipher(self):
        """Test cipher application."""
        mapping = {'A': 'B', 'B': 'A'}
        result = self.processor.apply_cipher("AB", mapping)
        assert result == "BA"
    
    def test_atbash_involution(self):
        """Test Atbash cipher involution property."""
        test_cases = ["A", "Z", "HELLO", "WORLD", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        
        for text in test_cases:
            assert self.processor.verify_involution(text, self.processor.atbash_mapping)
    
    def test_block_involution_default(self):
        """Test block cipher involution with default parts."""
        mapping = build_block_mapping()
        test_cases = ["A", "M", "N", "Z", "HELLO", "WORLD", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        
        for text in test_cases:
            assert self.processor.verify_involution(text, mapping)
    
    def test_block_involution_custom(self):
        """Test block cipher involution with custom parts."""
        part1 = "ABCDEF"
        part2 = "GHIJKLMNOPQRSTUVWXYZ"
        mapping = build_block_mapping(part1, part2)
        test_cases = ["A", "F", "G", "Z", "HELLO", "WORLD"]
        
        for text in test_cases:
            assert self.processor.verify_involution(text, mapping)
    
    def test_boundary_pairs_atbash(self):
        """Test boundary pairs in Atbash cipher."""
        mapping = self.processor.atbash_mapping
        assert mapping['A'] == 'Z'
        assert mapping['Z'] == 'A'
        assert mapping['M'] == 'N'
        assert mapping['N'] == 'M'
    
    def test_boundary_pairs_block(self):
        """Test boundary pairs in block cipher."""
        mapping = build_block_mapping()
        # Part 1 boundaries
        assert mapping['A'] == 'M'
        assert mapping['M'] == 'A'
        # Part 2 boundaries
        assert mapping['N'] == 'Z'
        assert mapping['Z'] == 'N'
    
    def test_process_atbash(self):
        """Test complete Atbash processing."""
        results = self.processor.process_atbash("HELLO")
        assert results['normalized'] == "HELLO"
        assert results['ciphertext'] == "SVOOL"  # H->S, E->V, L->O, L->O, O->L
        assert results['direct_numbers'] == [8, 5, 12, 12, 15]
        assert results['reverse_numbers'] == [19, 22, 15, 15, 12]
        assert 'single_time_us' in results
        assert 'avg_time_per_char_us' in results
    
    def test_process_block(self):
        """Test complete block processing."""
        results = self.processor.process_block("HELLO")
        assert results['normalized'] == "HELLO"
        # H->F (part1), E->I (part1), L->B (part1), L->B (part1), O->Y (part2)
        assert results['ciphertext'] == "FIBBY"
        assert results['direct_numbers'] == [8, 5, 12, 12, 15]
        assert 'single_time_us' in results
        assert 'avg_time_per_char_us' in results
    
    def test_empty_input(self):
        """Test handling of empty input."""
        results = self.processor.process_atbash("")
        assert results['normalized'] == ""
        assert results['ciphertext'] == ""
        assert results['direct_numbers'] == []
        assert results['reverse_numbers'] == []


class TestPropertyBased:
    """Property-based tests."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.processor = CipherProcessor()
    
    @pytest.mark.parametrize("text", [
        "A", "Z", "HELLO", "WORLD", "TESTING", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "SMITH", "JONES", "BROWN", "WILSON"
    ])
    def test_atbash_involution_property(self, text):
        """Property test: Atbash is its own inverse."""
        if not HAS_PYTEST:
            # Run with sample data when pytest not available
            for text in ["HELLO", "WORLD", "SMITH"]:
                self._test_atbash_involution_single(text)
            return
        
        normalized = self.processor.normalize_input(text)
        encrypted = self.processor.apply_cipher(normalized, self.processor.atbash_mapping)
        decrypted = self.processor.apply_cipher(encrypted, self.processor.atbash_mapping)
        assert normalized == decrypted
    
    def _test_atbash_involution_single(self, text):
        """Helper for testing single case without pytest."""
        normalized = self.processor.normalize_input(text)
        encrypted = self.processor.apply_cipher(normalized, self.processor.atbash_mapping)
        decrypted = self.processor.apply_cipher(encrypted, self.processor.atbash_mapping)
        assert normalized == decrypted
    
    @pytest.mark.parametrize("text", [
        "A", "Z", "HELLO", "WORLD", "TESTING", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "SMITH", "JONES", "BROWN", "WILSON"
    ])
    def test_block_involution_property(self, text):
        """Property test: Block cipher is its own inverse."""
        if not HAS_PYTEST:
            # Run with sample data when pytest not available
            for text in ["HELLO", "WORLD", "SMITH"]:
                self._test_block_involution_single(text)
            return
            
        mapping = build_block_mapping()
        normalized = self.processor.normalize_input(text)
        encrypted = self.processor.apply_cipher(normalized, mapping)
        decrypted = self.processor.apply_cipher(encrypted, mapping)
        assert normalized == decrypted
    
    def _test_block_involution_single(self, text):
        """Helper for testing single case without pytest."""
        mapping = build_block_mapping()
        normalized = self.processor.normalize_input(text)
        encrypted = self.processor.apply_cipher(normalized, mapping)
        decrypted = self.processor.apply_cipher(encrypted, mapping)
        assert normalized == decrypted
    
    @pytest.mark.parametrize("text", [
        "hello world!", "Test123", "UPPER_CASE", "mixed123CASE!"
    ])
    def test_normalization_property(self, text):
        """Property test: Normalization removes non-letters and uppercases."""
        if not HAS_PYTEST:
            # Run with sample data when pytest not available
            for text in ["hello world!", "Test123"]:
                self._test_normalization_single(text)
            return
            
        normalized = self.processor.normalize_input(text)
        assert normalized.isalpha()
        assert normalized.isupper()
        # All original letters should be preserved (in uppercase)
        original_letters = ''.join(c.upper() for c in text if c.isalpha())
        assert normalized == original_letters
    
    def _test_normalization_single(self, text):
        """Helper for testing single case without pytest."""
        normalized = self.processor.normalize_input(text)
        assert normalized.isalpha()
        assert normalized.isupper()
        # All original letters should be preserved (in uppercase)
        original_letters = ''.join(c.upper() for c in text if c.isalpha())
        assert normalized == original_letters


def run_manual_tests():
    """Run tests manually when pytest is not available."""
    if HAS_PYTEST:
        pytest.main([__file__])
        return
    
    print("Running manual tests...")
    
    # Test mappings
    print("Testing mappings...")
    test_mappings = TestMappings()
    test_mappings.test_atbash_mapping()
    test_mappings.test_block_mapping_default()
    test_mappings.test_block_mapping_custom()
    test_mappings.test_direct_numbers()
    test_mappings.test_reverse_numbers()
    print("✓ Mapping tests passed")
    
    # Test cipher processor
    print("Testing cipher processor...")
    test_cipher = TestCipherProcessor()
    test_cipher.setup_method()
    test_cipher.test_normalize_input()
    test_cipher.test_apply_cipher()
    test_cipher.test_atbash_involution()
    test_cipher.test_block_involution_default()
    test_cipher.test_boundary_pairs_atbash()
    test_cipher.test_boundary_pairs_block()
    test_cipher.test_process_atbash()
    test_cipher.test_process_block()
    test_cipher.test_empty_input()
    print("✓ Cipher processor tests passed")
    
    # Test properties
    print("Testing properties...")
    test_props = TestPropertyBased()
    test_props.setup_method()
    test_props.test_atbash_involution_property("HELLO")
    test_props.test_block_involution_property("HELLO")
    test_props.test_normalization_property("hello world!")
    print("✓ Property tests passed")
    
    print("All tests completed successfully!")


if __name__ == '__main__':
    run_manual_tests()