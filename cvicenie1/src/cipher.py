#!/usr/bin/env python3
"""
Laboratory work No. 1 - Fundamentals of Cryptography
Student: Maros Bednar

This program implements stream coding (task 1a) and block coding (task 1b)
for encoding information messages using English alphabet.
"""
import argparse
import time
import sys
import os
from typing import Dict, List, Tuple

# Add current directory to path for relative imports
sys.path.insert(0, os.path.dirname(__file__))

from mappings import (
    build_atbash_mapping,
    build_block_mapping,
    get_direct_numbers,
    get_reverse_numbers,
    format_mapping_table,
    get_part_tables,
)


class CipherProcessor:
    """Class for processing both stream and block ciphers"""
    
    def __init__(self):
        # Build the stream cipher mapping (reverse alphabet)
        self.atbash_mapping = build_atbash_mapping()
    
    def normalize_input(self, text: str) -> str:
        """Convert text to uppercase and keep only letters"""
        result = ""
        for char in text:
            if char.isalpha():
                result += char.upper()
        return result
    
    def apply_cipher(self, text: str, mapping: Dict[str, str]) -> str:
        """Apply cipher mapping to each letter in text"""
        result = ""
        for char in text:
            if char in mapping:
                result += mapping[char]
            else:
                result += char  # keep non-mapped characters as is
        return result
    
    def time_cipher_operation(self, text: str, mapping: Dict[str, str]) -> Tuple[float, float]:
        """Measure time for cipher operation"""
        # Time single operation
        start = time.perf_counter()
        self.apply_cipher(text, mapping)
        end = time.perf_counter()
        single_time = (end - start) * 1000000  # convert to microseconds
        
        # Time multiple operations for average
        iterations = 10000
        start = time.perf_counter()
        for i in range(iterations):
            self.apply_cipher(text, mapping)
        end = time.perf_counter()
        
        total_time = (end - start) * 1000000
        avg_per_operation = total_time / iterations
        avg_per_char = avg_per_operation / len(text) if text else 0
        
        return single_time, avg_per_char
    
    def process_atbash(self, surname: str) -> Dict:
        """
        Process surname using Atbash cipher.
        
        Args:
            surname: Input surname
        
        Returns:
            Dictionary with all results.
        """
        normalized = self.normalize_input(surname)
        ciphertext = self.apply_cipher(normalized, self.atbash_mapping)
        direct_nums = get_direct_numbers(normalized)
        reverse_nums = get_reverse_numbers(normalized)
        
        single_time, avg_time_per_char = self.time_cipher_operation(normalized, self.atbash_mapping)
        
        return {
            'normalized': normalized,
            'ciphertext': ciphertext,
            'direct_numbers': direct_nums,
            'reverse_numbers': reverse_nums,
            'single_time_us': single_time,
            'avg_time_per_char_us': avg_time_per_char,
            'mapping_table': format_mapping_table(self.atbash_mapping, "Atbash Cipher (A↔Z)")
        }
    
    def process_block(self, surname: str, part1: str = "ABCDEFGHIJKLM", part2: str = "NOPQRSTUVWXYZ") -> Dict:
        """
        Process surname using block cipher.
        
        Args:
            surname: Input surname
            part1: First part of alphabet
            part2: Second part of alphabet
        
        Returns:
            Dictionary with all results.
        """
        normalized = self.normalize_input(surname)
        block_mapping = build_block_mapping(part1, part2)
        ciphertext = self.apply_cipher(normalized, block_mapping)
        direct_nums = get_direct_numbers(normalized)
        
        single_time, avg_time_per_char = self.time_cipher_operation(normalized, block_mapping)
        part1_table, part2_table = get_part_tables(part1, part2)
        
        return {
            'normalized': normalized,
            'ciphertext': ciphertext,
            'direct_numbers': direct_nums,
            'single_time_us': single_time,
            'avg_time_per_char_us': avg_time_per_char,
            'part1_table': part1_table,
            'part2_table': part2_table,
            'part1': part1,
            'part2': part2
        }
    
    def verify_involution(self, text: str, mapping: Dict[str, str]) -> bool:
        """
        Verify that applying the cipher twice returns original text.
        
        Args:
            text: Original text
            mapping: Cipher mapping
        
        Returns:
            True if cipher is involution, False otherwise.
        """
        normalized = self.normalize_input(text)
        encrypted = self.apply_cipher(normalized, mapping)
        decrypted = self.apply_cipher(encrypted, mapping)
        return normalized == decrypted


def print_atbash_results(results: Dict, surname: str):
    """Print formatted results for Atbash cipher."""
    print(f"\n=== TASK 1a: ATBASH CIPHER (Stream Coding) ===")
    print(f"Input surname: {surname}")
    print(f"Normalized input: {results['normalized']}")
    print(results['mapping_table'])
    
    print(f"\nDirect numbers (A=1...Z=26):")
    for i, char in enumerate(results['normalized']):
        print(f"  {char} = {results['direct_numbers'][i]}")
    
    print(f"\nReverse numbers (A=26...Z=1):")
    for i, char in enumerate(results['normalized']):
        print(f"  {char} = {results['reverse_numbers'][i]}")
    
    print(f"\nCiphertext: {results['ciphertext']}")
    print(f"\nTiming:")
    print(f"  Single operation: {results['single_time_us']:.3f} μs")
    print(f"  Average per character (10,000 iterations): {results['avg_time_per_char_us']:.6f} μs/char")


def print_block_results(results: Dict, surname: str):
    """Print formatted results for block cipher."""
    print(f"\n=== TASK 1b: BLOCK CIPHER (Block Coding) ===")
    print(f"Input surname: {surname}")
    print(f"Normalized input: {results['normalized']}")
    print(f"\nAlphabet split: {results['part1']} | {results['part2']}")
    print(f"\n{results['part1_table']}")
    print(f"{results['part2_table']}")
    
    print(f"Direct numbers (A=1...Z=26):")
    for i, char in enumerate(results['normalized']):
        print(f"  {char} = {results['direct_numbers'][i]}")
    
    print(f"\nCiphertext: {results['ciphertext']}")
    print(f"\nTiming:")
    print(f"  Single operation: {results['single_time_us']:.3f} μs")
    print(f"  Average per character (10,000 iterations): {results['avg_time_per_char_us']:.6f} μs/char")


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(description='Cipher processor for cryptography lab work')
    parser.add_argument('--surname', required=True, help='Surname to encode')
    parser.add_argument('--mode', choices=['stream', 'block'], required=True, help='Cipher mode')
    parser.add_argument('--part1', default='ABCDEFGHIJKLM', help='First part for block cipher')
    parser.add_argument('--part2', default='NOPQRSTUVWXYZ', help='Second part for block cipher')
    
    args = parser.parse_args()
    
    processor = CipherProcessor()
    
    if args.mode == 'stream':
        results = processor.process_atbash(args.surname)
        print_atbash_results(results, args.surname)
        
        # Verify involution
        is_involution = processor.verify_involution(args.surname, processor.atbash_mapping)
        print(f"\nInvolution test: {'PASSED' if is_involution else 'FAILED'}")
        
    elif args.mode == 'block':
        results = processor.process_block(args.surname, args.part1, args.part2)
        print_block_results(results, args.surname)
        
        # Verify involution
        block_mapping = build_block_mapping(args.part1, args.part2)
        is_involution = processor.verify_involution(args.surname, block_mapping)
        print(f"\nInvolution test: {'PASSED' if is_involution else 'FAILED'}")


if __name__ == '__main__':
    main()