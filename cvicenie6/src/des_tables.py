"""
DES Tables and Permutations
Contains all the tables needed for simplified DES operations.
"""

# Initial bit permutation (IP) - Intel x86 format
# Reading from the image carefully, row by row
IP_INTEL_X86 = [
    6, 14, 22, 30, 38, 46, 54, 62,
    4, 12, 20, 28, 36, 44, 52, 60,
    2, 10, 18, 26, 34, 42, 50, 58,
    0, 8, 16, 24, 32, 40, 48, 56,
    7, 15, 23, 31, 39, 47, 55, 63,
    5, 13, 21, 29, 37, 45, 53, 61,
    3, 11, 19, 27, 35, 43, 51, 59,
    1, 9, 17, 25, 33, 41, 49, 57
]

# Final bit permutation (IP⁻¹) - Intel x86 format
# Reading from the image carefully, row by row
IP_INVERSE_INTEL_X86 = [
    24, 56, 16, 48, 8, 40, 0, 32,
    25, 57, 17, 49, 9, 41, 1, 33,
    26, 58, 18, 50, 10, 42, 2, 34,
    27, 59, 19, 51, 11, 43, 3, 35,
    28, 60, 20, 52, 12, 44, 4, 36,
    29, 61, 21, 53, 13, 45, 5, 37,
    30, 62, 22, 54, 14, 46, 6, 38,
    31, 63, 23, 55, 15, 47, 7, 39
]

# IP cob permutation - mental table from USTAŠI
# Reading from the table in exercise 1, specification 3
# Values are 1-indexed in the table, converted to 0-indexed here
IP_COB_RAW = [
    16, 19, 5, 1, 13,
    14, 4, 21, 10, 8,
    24, 11, 3, 12, 22,
    17, 9, 20, 7, 18,
    23, 2, 6, 15, 25
]
# Convert to 0-indexed
IP_COB = [x - 1 for x in IP_COB_RAW]

# The second DES S-box (given in exercise 3)
# Reading row by row, column by column from the image
S_BOX_2 = [
    # Row 0
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    # Row 1
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    # Row 2
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    # Row 3
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]


def apply_permutation(data, permutation_table):
    """
    Apply a permutation to input data.
    
    Args:
        data: List of bits or string of '0' and '1'
        permutation_table: List of indices for permutation
        
    Returns:
        List of permuted bits
    """
    if isinstance(data, str):
        data = [int(b) for b in data]
    
    return [data[i] for i in permutation_table]


def apply_inverse_permutation(data, permutation_table):
    """
    Apply inverse permutation.
    
    Args:
        data: List of bits or string of '0' and '1'
        permutation_table: Original permutation table
        
    Returns:
        List of bits after inverse permutation
    """
    if isinstance(data, str):
        data = [int(b) for b in data]
    
    # Create inverse permutation
    inverse = [0] * len(permutation_table)
    for new_pos, old_pos in enumerate(permutation_table):
        inverse[old_pos] = new_pos
    
    return [data[i] for i in inverse]


def s_box_lookup(s_box, input_bits):
    """
    Perform S-box lookup.
    
    Args:
        s_box: 2D array representing the S-box
        input_bits: 6-bit input (as list or string)
        
    Returns:
        4-bit output value
    """
    if isinstance(input_bits, str):
        input_bits = [int(b) for b in input_bits]
    
    if len(input_bits) != 6:
        raise ValueError("S-box input must be 6 bits")
    
    # Row is determined by outer bits (first and last)
    row = (input_bits[0] << 1) | input_bits[5]
    
    # Column is determined by middle 4 bits
    col = (input_bits[1] << 3) | (input_bits[2] << 2) | (input_bits[3] << 1) | input_bits[4]
    
    # Look up value
    value = s_box[row][col]
    
    # Convert to 4-bit binary
    return [(value >> i) & 1 for i in range(3, -1, -1)]


def bits_to_string(bits):
    """Convert list of bits to string."""
    return ''.join(str(b) for b in bits)


def bits_to_int(bits):
    """Convert list of bits to integer."""
    result = 0
    for bit in bits:
        result = (result << 1) | bit
    return result
