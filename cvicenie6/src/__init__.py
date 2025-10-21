"""
ZKGRA Lab 6 - Simplified DES Operations
Core functionality for DES permutations and S-box lookups.
"""

from .des_tables import (
    IP_INTEL_X86,
    IP_INVERSE_INTEL_X86,
    IP_COB,
    S_BOX_2,
    apply_permutation,
    apply_inverse_permutation,
    s_box_lookup,
    bits_to_string,
    bits_to_int
)

__all__ = [
    'IP_INTEL_X86',
    'IP_INVERSE_INTEL_X86',
    'IP_COB',
    'S_BOX_2',
    'apply_permutation',
    'apply_inverse_permutation',
    's_box_lookup',
    'bits_to_string',
    'bits_to_int'
]
