"""
Functions for creating cipher mappings
Laboratory work No. 1
"""
from typing import Dict, Tuple


def build_atbash_mapping() -> Dict[str, str]:
    """Build mapping for stream cipher (reverse alphabet)"""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reversed_alphabet = alphabet[::-1]  # reverse the alphabet
    
    # Create mapping dictionary
    mapping = {}
    for i in range(26):
        mapping[alphabet[i]] = reversed_alphabet[i]
    
    return mapping


def build_block_mapping(part1: str = "ABCDEFGHIJKLM", part2: str = "NOPQRSTUVWXYZ") -> Dict[str, str]:
    """Build mapping for block cipher (reverse within each part)"""
    mapping = {}
    
    # Reverse first part
    reversed_part1 = part1[::-1]
    for i in range(len(part1)):
        mapping[part1[i]] = reversed_part1[i]
    
    # Reverse second part  
    reversed_part2 = part2[::-1]
    for i in range(len(part2)):
        mapping[part2[i]] = reversed_part2[i]
    
    return mapping


def get_direct_numbers(text: str) -> list[int]:
    """Get direct numbering A=1, B=2, ..., Z=26"""
    numbers = []
    for char in text:
        if char.isalpha():
            number = ord(char.upper()) - ord('A') + 1
            numbers.append(number)
    return numbers


def get_reverse_numbers(text: str) -> list[int]:
    """Get reverse numbering A=26, B=25, ..., Z=1"""
    numbers = []
    for char in text:
        if char.isalpha():
            number = 26 - (ord(char.upper()) - ord('A'))
            numbers.append(number)
    return numbers


def format_mapping_table(mapping: Dict[str, str], title: str) -> str:
    """
    Format a mapping dictionary as a readable table.
    
    Args:
        mapping: Letter-to-letter mapping
        title: Title for the table
    
    Returns:
        Formatted string representation of the mapping table.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_line = "".join(mapping[char] for char in alphabet)
    
    result = f"\n{title}:\n"
    result += "Plain:  " + " ".join(alphabet) + "\n"
    result += "Cipher: " + " ".join(cipher_line) + "\n"
    return result


def get_part_tables(part1: str, part2: str) -> Tuple[str, str]:
    """
    Get formatted tables for block cipher parts.
    
    Args:
        part1: First part of alphabet
        part2: Second part of alphabet
    
    Returns:
        Tuple of (part1_table, part2_table) formatted strings.
    """
    part1_reversed = part1[::-1]
    part2_reversed = part2[::-1]
    
    part1_table = f"Part 1 ({part1[0]}-{part1[-1]}):\n"
    part1_table += "Plain:  " + " ".join(part1) + "\n"
    part1_table += "Cipher: " + " ".join(part1_reversed) + "\n"
    
    part2_table = f"Part 2 ({part2[0]}-{part2[-1]}):\n"
    part2_table += "Plain:  " + " ".join(part2) + "\n"
    part2_table += "Cipher: " + " ".join(part2_reversed) + "\n"
    
    return part1_table, part2_table