"""
Entropy calculations for ZKGRA Lab Work 2.

This module provides entropy calculation for equiprobable distributions.
"""
import math


def entropy_equiprobable(n: int) -> float:
    """
    Calculate Shannon entropy for equiprobable distribution.
    
    For n equally likely outcomes, entropy H = log2(n).
    
    Args:
        n: Number of equally likely outcomes (must be positive)
        
    Returns:
        Entropy in bits (log2(n))
        
    Raises:
        ValueError: If n is not positive
        
    Examples:
        entropy_equiprobable(8) returns 3.0 (2^3 = 8)
        entropy_equiprobable(128) returns 7.0 (2^7 = 128)
        entropy_equiprobable(10) returns approximately 3.321928
    """
    if n <= 0:
        raise ValueError("n must be positive")
    
    return math.log2(n)
