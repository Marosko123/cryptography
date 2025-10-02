"""
Polybius Square (6x6) implementation for ZKGRA Lab Work 2.

This module provides encoding and decoding functionality using a 6x6 Polybius square
that includes A-Z letters and 0-9 digits.
"""
import unicodedata
from typing import Tuple


# Hardcoded 6x6 Polybius grid (row, column both 1-based)
POLYBIUS_GRID = {
    'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15', 'F': '16',
    'G': '21', 'H': '22', 'I': '23', 'J': '24', 'K': '25', 'L': '26',
    'M': '31', 'N': '32', 'O': '33', 'P': '34', 'Q': '35', 'R': '36',
    'S': '41', 'T': '42', 'U': '43', 'V': '44', 'W': '45', 'X': '46',
    'Y': '51', 'Z': '52', '0': '53', '1': '54', '2': '55', '3': '56',
    '4': '61', '5': '62', '6': '63', '7': '64', '8': '65', '9': '66',
}

# Reverse mapping for decoding
REVERSE_GRID = {v: k for k, v in POLYBIUS_GRID.items()}


def remove_diacritics(text: str) -> str:
    """
    Remove diacritics from text using unicodedata.
    
    Args:
        text: Input text that may contain diacritics
        
    Returns:
        Text with diacritics removed (e.g., "Á" -> "A", "Č" -> "C")
    """
    # Normalize to NFD (decomposed form) then filter out combining marks
    nfd = unicodedata.normalize('NFD', text)
    result = ''
    for char in nfd:
        if unicodedata.category(char) != 'Mn':  # Mn = Mark, Nonspacing
            result += char
    return result


def normalize_text(text: str) -> str:
    """
    Normalize text for Polybius encoding.
    
    Args:
        text: Input text
        
    Returns:
        Uppercase text with diacritics removed
    """
    text = remove_diacritics(text)
    return text.upper()


def encode(text: str) -> Tuple[str, str]:
    """
    Encode text using Polybius square.
    
    Args:
        text: Input text (A-Z, 0-9, spaces, Slovak diacritics allowed)
        
    Returns:
        Tuple of (space-separated pairs, concatenated string)
        Spaces in input are preserved as spaces in output
        
    Examples:
        encode("ENCRYPT ME 2 DAY") returns:
            ("15 32 13 36 51 34 42  31 15  55  14 11 51",
             "15321336513442 3115 55 141151")
    """
    normalized = normalize_text(text)
    
    pairs_parts = []
    concatenated = []
    
    for char in normalized:
        if char == ' ':
            # Add empty string to create double space when joined
            pairs_parts.append('')
            concatenated.append(' ')
        elif char in POLYBIUS_GRID:
            code = POLYBIUS_GRID[char]
            pairs_parts.append(code)
            concatenated.append(code)
    
    pairs_str = ' '.join(pairs_parts)
    concat_str = ''.join(concatenated)
    
    return pairs_str, concat_str


def decode(pairs_string: str) -> str:
    """
    Decode Polybius-encoded text.
    
    Args:
        pairs_string: Space-separated pairs of digits (e.g., "15 32 13")
                     Spaces are preserved, non-2-digit tokens are ignored
        
    Returns:
        Decoded plaintext with spaces preserved
        
    Examples:
        decode("15 32 13 36 51 34 42") returns "ENCRYPT"
    """
    tokens = pairs_string.split(' ')
    result = []
    
    for token in tokens:
        if token == '':
            # Empty token from consecutive spaces
            result.append(' ')
        elif len(token) == 2 and token.isdigit():
            # Valid 2-digit code
            if token in REVERSE_GRID:
                result.append(REVERSE_GRID[token])
        elif not token.isdigit():
            # Preserve spaces or other non-digit separators
            result.append(' ')
    
    return ''.join(result)
