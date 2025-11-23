def calculate_parity_bit(binary_string: str) -> str:
    """
    Calculates the parity bit for a binary string.
    The bit is the sum of the values of the previous symbols (modulo two).
    """
    sum_val = 0
    for char in binary_string:
        if char == '1':
            sum_val += 1
    
    return str(sum_val % 2)

def encode_redundant(binary_code: str) -> str:
    """
    Appends the parity bit to the binary code.
    """
    return binary_code + calculate_parity_bit(binary_code)

def get_non_redundant_codes():
    return {
        "A1": "00",
        "A2": "01",
        "A3": "10",
        "A4": "11",
        "A5": "100",
        "A6": "101"
    }
