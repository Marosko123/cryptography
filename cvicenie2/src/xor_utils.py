"""
XOR utilities for ZKGRA Lab Work 2.

This module provides XOR operations on bitstrings and evaluation of XOR expressions.
"""
from typing import List


def xor_chain(*bitstrings: str) -> str:
    """
    XOR multiple bitstrings of the same length.
    
    Args:
        *bitstrings: Variable number of bitstring arguments (e.g., "1011", "0110")
                    All must be the same length and contain only '0' and '1'
        
    Returns:
        XOR result as a bitstring
        
    Raises:
        ValueError: If bitstrings are not the same length or contain invalid characters
        
    Examples:
        xor_chain("1011", "0110") returns "1101"
        xor_chain("1011", "0110", "0100") returns "1001"
    """
    if not bitstrings:
        raise ValueError("At least one bitstring is required")
    
    # Validate all bitstrings
    length = len(bitstrings[0])
    for bs in bitstrings:
        if len(bs) != length:
            raise ValueError(f"All bitstrings must be the same length (expected {length}, got {len(bs)})")
        if not all(c in '01' for c in bs):
            raise ValueError(f"Bitstring must contain only '0' and '1': {bs}")
    
    # Perform XOR
    result = [int(c) for c in bitstrings[0]]
    
    for bs in bitstrings[1:]:
        for i, c in enumerate(bs):
            result[i] ^= int(c)
    
    return ''.join(str(b) for b in result)


def evaluate_expression(a: str, b: str, c: str) -> str:
    """
    Evaluate the XOR expression: a XOR b XOR c XOR a XOR b
    
    This simplifies to just c (since a XOR a = 0, b XOR b = 0).
    
    Args:
        a: First bitstring
        b: Second bitstring
        c: Third bitstring
        
    Returns:
        Result of a ⊕ b ⊕ c ⊕ a ⊕ b
        
    Examples:
        evaluate_expression("1011", "0110", "0100") returns "0100"
        evaluate_expression("0101", "1110", "1101") returns "1101"
    """
    # Mathematically: a ⊕ b ⊕ c ⊕ a ⊕ b = c
    # But we'll compute it explicitly to demonstrate
    return xor_chain(a, b, c, a, b)
