import random
import hashlib
import math

def is_prime(n, k=5):
    """Miller-Rabin primality test."""
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    """Generate a prime number with specified bits."""
    while True:
        n = random.getrandbits(bits)
        # Ensure it's odd and has the right bit length
        n |= (1 << (bits - 1)) | 1
        if is_prime(n):
            return n

def generate_parameters(p_bits=64, q_bits=32):
    """
    Generate Schnorr parameters p, q, g.
    q: prime divisor of p-1
    p: prime
    g: generator of order q
    """
    # 1. Generate q
    q = generate_prime(q_bits)
    
    # 2. Find p such that q divides p-1 => p = k*q + 1
    # We want p to be p_bits long.
    # k approx 2^p_bits / q
    k_min = (1 << (p_bits - 1)) // q
    k_max = (1 << p_bits) // q
    
    while True:
        k = random.randint(k_min, k_max)
        # Ensure k is even so p is odd (since q is odd)
        if k % 2 != 0:
            k += 1
            
        p = k * q + 1
        if p.bit_length() == p_bits and is_prime(p):
            break
            
    # 3. Find g
    # g = h^((p-1)/q) mod p, where h is random, g != 1
    while True:
        h = random.randint(2, p - 2)
        g = pow(h, (p - 1) // q, p)
        if g != 1:
            break
            
    return p, q, g

def mod_inverse(a, m):
    """Calculate modular multiplicative inverse of a modulo m."""
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = extended_gcd(b % a, a)
            return g, x - (b // a) * y, y

    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

class Schnorr:
    def __init__(self, p=None, q=None, g=None):
        if p is None:
            # Default small parameters for demonstration if not provided
            # Using small bits for speed in this exercise
            self.p, self.q, self.g = generate_parameters(64, 32)
        else:
            self.p = p
            self.q = q
            self.g = g
            
    def generate_keys(self):
        """
        Generate private key x and public key y.
        x: random in [1, q-1]
        y: g^(-x) mod p
        """
        self.x = random.randint(1, self.q - 1)
        # y = g^(-x) = (g^x)^(-1) mod p
        g_x = pow(self.g, self.x, self.p)
        self.y = mod_inverse(g_x, self.p)
        return self.x, self.y
    
    def hash_function(self, r, message):
        """
        Hash function H(r, M).
        Returns integer.
        """
        # Convert r to bytes
        r_bytes = str(r).encode()
        msg_bytes = message.encode() if isinstance(message, str) else message
        
        hasher = hashlib.sha256()
        hasher.update(r_bytes)
        hasher.update(msg_bytes)
        digest = hasher.hexdigest()
        
        # Convert hex digest to integer
        return int(digest, 16)
        
    def sign(self, message):
        """
        Sign a message.
        Returns (e, s).
        """
        if not hasattr(self, 'x'):
            raise Exception("Keys not generated")
            
        # 1. Choose random k
        k = random.randint(1, self.q - 1)
        
        # Calculate r = g^k mod p
        r = pow(self.g, k, self.p)
        
        # 2. Calculate e = H(r, M)
        e = self.hash_function(r, message)
        
        # Calculate s = k + x*e
        # Note: s is not taken modulo q in the assignment formula "s = k + xe"
        # But usually in Schnorr s is mod q.
        # However, the verification r' = g^s * y^e mod p works even if s is not mod q,
        # because g^q = 1 mod p.
        # Let's follow the formula strictly: s = k + x*e
        s = k + self.x * e
        
        return e, s
        
    def verify(self, message, e, s, public_key_y):
        """
        Verify signature (e, s).
        Returns True if valid, False otherwise.
        """
        # 4. Calculate r' = g^s * y^e mod p
        # r' = (g^s * y^e) mod p
        term1 = pow(self.g, s, self.p)
        term2 = pow(public_key_y, e, self.p)
        r_prime = (term1 * term2) % self.p
        
        # Calculate e' = H(r', M)
        e_prime = self.hash_function(r_prime, message)
        
        # 5. Compare e and e'
        return e == e_prime

