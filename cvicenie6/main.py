#!/usr/bin/env python3
"""
ZKGRA - Laboratory Work No. 6
Simplified DES Operations

Student: Maroš Bednár (xbednarm1@stuba.sk)
Date: October 21, 2025
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from des_tables import (
    IP_INTEL_X86, IP_INVERSE_INTEL_X86, IP_COB, S_BOX_2,
    apply_permutation, s_box_lookup, bits_to_string, bits_to_int
)


def exercise_1():
    """
    Exercise 1: Encode information message using IP cob permutation.
    
    Message: USTAŠI
    Alphabet: A-Z (A=1, B=2, ..., Z=26)
    Note: Š is treated as one bit (skin letter)
    Student number: xbednarm1 (last digit = 1)
    
    Parts L and R are designated as subdivision throughout.
    """
    print("=" * 70)
    print("EXERCISE 1: Encode USTAŠI using IP cob permutation")
    print("=" * 70)
    
    # Map letters to numbers
    message = "USTAŠI"
    # U=21, S=19, T=20, A=1, Š=1 (skin letter, one bit), I=9
    
    # According to specification:
    # - Official number last digit = 1
    # - Š (skin letter) is one bit
    
    # Create bit representation
    # The mental table has 25 positions (5x5 grid)
    print(f"\nOriginal message: {message}")
    print(f"Student number last digit: 1")
    print(f"\nNote: Š (skin letter) is represented as one bit")
    
    # Map each letter to position in mental table
    # Based on the table given: positions 1-25
    letter_positions = {
        'U': 21, 'S': 19, 'T': 20, 'A': 1, 'Š': 1, 'I': 9
    }
    
    print(f"\nLetter to position mapping:")
    for letter in message:
        print(f"  {letter} -> {letter_positions[letter]}")
    
    # Create 25-bit message based on positions
    # Set bit at each position to 1
    bits = [0] * 25
    for letter in message:
        pos = letter_positions[letter] - 1  # Convert to 0-indexed
        bits[pos] = 1
    
    print(f"\nOriginal bit pattern (25 bits):")
    print(f"  {bits_to_string(bits)}")
    
    # Apply IP cob permutation
    permuted = apply_permutation(bits, IP_COB)
    
    print(f"\nAfter IP cob permutation:")
    print(f"  {bits_to_string(permuted)}")
    
    # Designation into L and R parts
    # For simplicity, split in middle
    mid = len(permuted) // 2
    L = permuted[:mid]
    R = permuted[mid:]
    
    print(f"\nSubdivision into L and R:")
    print(f"  L (left {len(L)} bits):  {bits_to_string(L)}")
    print(f"  R (right {len(R)} bits): {bits_to_string(R)}")
    
    return bits, permuted, L, R


def exercise_2():
    """
    Exercise 2: Fill correspondence table between Intel x86 and original DES
    permutation tables.
    
    Find correspondence for positions: 14, 23, 61, 6
    """
    print("\n" + "=" * 70)
    print("EXERCISE 2: Correspondence between Intel x86 and DES IP tables")
    print("=" * 70)
    
    # Create mapping from Intel x86 IP to original DES IP
    # Intel x86 IP tells us where each bit goes
    # We need to find where these positions come from in original DES
    
    # Create inverse of Intel x86 IP to find original positions
    intel_to_original_ip = {}
    for new_pos, old_pos in enumerate(IP_INTEL_X86):
        intel_to_original_ip[new_pos] = old_pos
    
    # Original DES IP (standard DES initial permutation)
    # Standard DES IP (1-indexed in literature, but we use 0-indexed)
    ORIGINAL_DES_IP = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    
    # Adjust to 0-indexed
    ORIGINAL_DES_IP = [x - 1 for x in ORIGINAL_DES_IP]
    
    positions_to_check = [14, 23, 61, 6]
    
    print("\nCorrespondence Table:")
    print("-" * 70)
    print(f"{'Intel x86 IP position':<25} {'Original DES IP position':<25} {'Final IP⁻¹ position':<25}")
    print("-" * 70)
    
    results = {}
    for pos in positions_to_check:
        # Where does position 'pos' in Intel x86 IP come from?
        original_pos = intel_to_original_ip[pos]
        
        # Find in original DES IP
        des_original = None
        for i, val in enumerate(ORIGINAL_DES_IP):
            if val == original_pos:
                des_original = i
                break
        
        # Find in final permutation (IP⁻¹)
        final_pos = None
        for i, val in enumerate(IP_INVERSE_INTEL_X86):
            if val == pos:
                final_pos = i
                break
        
        results[pos] = (des_original, final_pos)
        print(f"{pos:<25} {des_original:<25} {final_pos if final_pos else 'N/A':<25}")
    
    print("-" * 70)
    
    return results


def exercise_3():
    """
    Exercise 3: Calculate S-box transformations for given 6-bit inputs.
    
    Using the second S-box table.
    """
    print("\n" + "=" * 70)
    print("EXERCISE 3: S-box transformations")
    print("=" * 70)
    
    test_inputs = [
        "011010",  # A
        "001111",  # B
        "110110",  # C
        "110011",  # D
    ]
    
    print("\nUsing the second DES S-box:")
    print("-" * 70)
    
    results = {}
    for label, input_bits in zip(['A', 'B', 'C', 'D'], test_inputs):
        output = s_box_lookup(S_BOX_2, input_bits)
        output_str = bits_to_string(output)
        output_int = bits_to_int(output)
        
        # Detailed calculation
        bits = [int(b) for b in input_bits]
        row = (bits[0] << 1) | bits[5]
        col = (bits[1] << 3) | (bits[2] << 2) | (bits[3] << 1) | bits[4]
        
        results[label] = {
            'input': input_bits,
            'output': output_str,
            'decimal': output_int,
            'row': row,
            'col': col
        }
        
        print(f"\n{label}. Input: {input_bits}")
        print(f"   Row bits (outer): {bits[0]}...{bits[5]} = {row}")
        print(f"   Col bits (middle): {bits[1]}{bits[2]}{bits[3]}{bits[4]} = {col}")
        print(f"   S-box[{row}][{col}] = {output_int}")
        print(f"   Output (4 bits): {output_str}")
    
    print("\n" + "-" * 70)
    print("\nSummary:")
    for label in ['A', 'B', 'C', 'D']:
        r = results[label]
        print(f"  {label}. {r['input']} → {r['output']} (decimal: {r['decimal']})")
    
    return results


def main():
    """Main program - solve all exercises."""
    print("\n" + "=" * 70)
    print("ZKGRA - LABORATORY WORK NO. 6")
    print("Simplified DES Operations")
    print("=" * 70)
    print("\nStudent: Maroš Bednár (xbednarm1@stuba.sk)")
    print("Date: October 21, 2025")
    print("\nObjective: Modeling of coding algorithms using Feistel mesh transformation")
    print("=" * 70)
    
    # Exercise 1
    ex1_results = exercise_1()
    
    # Exercise 2
    ex2_results = exercise_2()
    
    # Exercise 3
    ex3_results = exercise_3()
    
    print("\n" + "=" * 70)
    print("ALL EXERCISES COMPLETED")
    print("=" * 70)
    
    return {
        'exercise_1': ex1_results,
        'exercise_2': ex2_results,
        'exercise_3': ex3_results
    }


if __name__ == "__main__":
    main()
