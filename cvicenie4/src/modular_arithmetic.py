"""
ZKGRA - Laboratory Work No. 4
Modular Arithmetic Operations

Student: Maroš Bednár (xbednarm1@stuba.sk)
"""

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    Returns (gcd, x, y) such that a*x + b*y = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y


def mod_inverse(a, m):
    """
    Calculate modular multiplicative inverse of a modulo m.
    Returns the inverse if it exists, None otherwise.
    
    The inverse exists only if gcd(a, m) = 1.
    """
    gcd, x, _ = extended_gcd(a % m, m)
    
    if gcd != 1:
        return None  # Modular inverse doesn't exist
    
    return (x % m + m) % m


def residual_vector(n, m):
    """
    Generate vector of residuals: [n^1 mod m, n^2 mod m, n^3 mod m, ...]
    Stops when the pattern starts repeating.
    
    Args:
        n: base number
        m: modulus
        
    Returns:
        list of residuals until the cycle repeats
    """
    vector = []
    seen = set()
    i = 1
    
    while True:
        residual = pow(n, i, m)  # Efficient modular exponentiation
        
        if residual in seen:
            break
            
        vector.append(residual)
        seen.add(residual)
        i += 1
        
        # Safety limit to prevent infinite loops
        if i > m:
            break
    
    return vector


def diffie_hellman_exchange(g, p, secret_a, secret_b):
    """
    Perform Diffie-Hellman key exchange.
    
    Args:
        g: generator (base function)
        p: modulus
        secret_a: Alice's secret key
        secret_b: Bob's secret key
        
    Returns:
        tuple: (public_a, public_b, shared_key_alice, shared_key_bob)
    """
    # Step 1: Alice computes her public key
    public_a = pow(g, secret_a, p)
    
    # Step 2: Bob computes his public key
    public_b = pow(g, secret_b, p)
    
    # Step 3: Alice computes shared secret using Bob's public key
    shared_alice = pow(public_b, secret_a, p)
    
    # Step 4: Bob computes shared secret using Alice's public key
    shared_bob = pow(public_a, secret_b, p)
    
    return public_a, public_b, shared_alice, shared_bob


def gcd(a, b):
    """Calculate greatest common divisor."""
    while b:
        a, b = b, a % b
    return a
