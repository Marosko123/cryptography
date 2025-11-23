import random
from .des_tables import IP_INTEL_X86, IP_INVERSE_INTEL_X86

def get_parameters(parity_n, parity_m, count_n=1):
    """
    Get parameters n and m from IP tables based on parity.
    parity_n: 'even' or 'odd'
    parity_m: 'even' or 'odd'
    count_n: number of n values to return (for n1..n6)
    """
    all_values = IP_INTEL_X86 + IP_INVERSE_INTEL_X86
    
    # Filter by parity
    n_candidates = [x for x in all_values if (x % 2 == 0 if parity_n == 'even' else x % 2 != 0)]
    m_candidates = [x for x in all_values if (x % 2 == 0 if parity_m == 'even' else x % 2 != 0)]
    
    if not n_candidates or not m_candidates:
        raise ValueError("Could not find values satisfying parity conditions")
        
    # Select random values
    # Ensure we have enough unique values if possible, otherwise allow duplicates
    if len(n_candidates) < count_n:
        ns = [random.choice(n_candidates) for _ in range(count_n)]
    else:
        ns = random.sample(n_candidates, count_n)
        
    m = random.choice(m_candidates)
    
    if count_n == 1:
        return ns[0], m
    return ns, m

def hash_1(n, m):
    """h(n) = n mod m"""
    return n % m

def hash_2(n_list, m):
    """h(n) = (h(n1) + ... + h(n6)) mod m"""
    # Note: The formula says h(n) = (h(n1) + ... + h(n6)) mod m
    # But h(x) is defined as x mod m in 1.1.
    # So it is likely sum(ni mod m) mod m
    
    sum_h = sum(hash_1(ni, m) for ni in n_list)
    return sum_h % m

def custom_hash(text):
    """
    A simple custom hash function for strings.
    Uses a combination of XOR, shifting and modular arithmetic.
    """
    hash_val = 0x55555555  # Initial seed
    prime = 31
    
    for char in text:
        byte_val = ord(char)
        # Rotate left 5 bits
        hash_val = ((hash_val << 5) | (hash_val >> 27)) & 0xFFFFFFFF
        # XOR with byte value
        hash_val ^= byte_val
        # Multiply by prime
        hash_val = (hash_val * prime) & 0xFFFFFFFF
        
    return hex(hash_val)[2:]
