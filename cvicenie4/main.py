#!/usr/bin/env python3
"""
ZKGRA - Laboratory Work No. 4 - Main Program
Solves all exercises programmatically

Student: Maroš Bednár (xbednarm1@stuba.sk)
Date: October 21, 2025
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from modular_arithmetic import mod_inverse, residual_vector, diffie_hellman_exchange, gcd


def print_header(text, char="="):
    """Print formatted header."""
    width = 70
    print(f"\n{char * width}")
    print(text)
    print(f"{char * width}\n")


def exercise_1():
    """Solve Exercise 1: Modular operations."""
    print_header("EXERCISE 1: Modular Operations")
    
    # Part 1: Simple modulo operations
    print("1. Simple modulo operations:")
    operations = [
        (2, 4),
        (78, 33),
        (51, 7),
        (27, 47)
    ]
    
    for a, m in operations:
        result = a % m
        print(f"   {a} mod {m} = {result}")
    
    # Part 2: Modular inverse operations
    print("\n2. Modular inverse operations:")
    inverse_operations = [
        (7, 47),
        (19, 7),
        (4, 7),
        (4, 15),
        (3, 7),
        (4, 17),
        (9, 17),
        (2, 6)
    ]
    
    for a, m in inverse_operations:
        inv = mod_inverse(a, m)
        
        if inv is not None:
            # Verify the result
            verification = (a * inv) % m
            print(f"   {a}^-1 mod {m} = {inv}")
            print(f"      Verification: {a} × {inv} ≡ {verification} (mod {m})")
        else:
            g = gcd(a, m)
            print(f"   {a}^-1 mod {m} = Does not exist")
            print(f"      Reason: gcd({a}, {m}) = {g} ≠ 1")


def exercise_2():
    """Solve Exercise 2: Vector of residuals."""
    print_header("EXERCISE 2: Vector of Residuals")
    
    problems = [
        (4, 9, "2.1"),
        (15, 7, "2.2"),
        (32, 29, "2.3")
    ]
    
    for n, m, label in problems:
        vector = residual_vector(n, m)
        print(f"{label}. Vector of residuals of {n} by modulus {m}:")
        print(f"     Powers: ", end="")
        
        # Show first few powers explicitly
        show_count = min(3, len(vector))
        for i in range(show_count):
            print(f"{n}^{i+1} mod {m} = {vector[i]}", end="")
            if i < show_count - 1:
                print(", ", end="")
        
        if len(vector) > show_count:
            print(", ...")
        else:
            print()
        
        print(f"     Vector: {vector}")
        print(f"     Length: {len(vector)} (cycle repeats after this)")
        print()


def exercise_3():
    """Solve Exercise 3: Asymmetric encryption (Diffie-Hellman)."""
    print_header("EXERCISE 3: Asymmetric Encryption")
    
    print("Given:")
    print("   - Alice's (transmitter) secret key: a = 6")
    print("   - Bob's (receiver) secret key: b = 3")
    
    alice_secret = 6
    bob_secret = 3
    
    # Problem 3.1a
    print("\n3.1.a) Function: 2^x (mod 4)")
    print("-" * 40)
    
    g1, p1 = 2, 4
    pub_a1, pub_b1, shared_a1, shared_b1 = diffie_hellman_exchange(
        g1, p1, alice_secret, bob_secret
    )
    
    print(f"   Alice computes: 2^{alice_secret} mod {p1} = {pub_a1}")
    print(f"   Alice sends {pub_a1} to Bob")
    print()
    print(f"   Bob computes: 2^{bob_secret} mod {p1} = {pub_b1}")
    print(f"   Bob sends {pub_b1} to Alice")
    print()
    print(f"   Alice's shared key: {pub_b1}^{alice_secret} mod {p1} = {shared_a1}")
    print(f"   Bob's shared key: {pub_a1}^{bob_secret} mod {p1} = {shared_b1}")
    print()
    
    if shared_a1 == shared_b1:
        print(f"   Shared secret key: {shared_a1}")
    else:
        print(f"   ✗ Keys don't match! Alice: {shared_a1}, Bob: {shared_b1}")
    
    print(f"\n   Analysis: This is NOT suitable for DH because:")
    print(f"   - Modulus {p1} is too small (not secure)")
    print(f"   - 2^2 ≡ 0 (mod 4), so all powers ≥ 2 give 0")
    print(f"   - Shared key is always 0 (no security)")
    
    # Problem 3.1b
    print("\n3.1.b) Function: 78^x (mod 33)")
    print("-" * 40)
    
    g2, p2 = 78, 33
    pub_a2, pub_b2, shared_a2, shared_b2 = diffie_hellman_exchange(
        g2, p2, alice_secret, bob_secret
    )
    
    print(f"   Note: 78 mod 33 = {g2 % p2}")
    print()
    print(f"   Alice computes: 78^{alice_secret} mod {p2} = {pub_a2}")
    print(f"   Alice sends {pub_a2} to Bob")
    print()
    print(f"   Bob computes: 78^{bob_secret} mod {p2} = {pub_b2}")
    print(f"   Bob sends {pub_b2} to Alice")
    print()
    print(f"   Alice's shared key: {pub_b2}^{alice_secret} mod {p2} = {shared_a2}")
    print(f"   Bob's shared key: {pub_a2}^{bob_secret} mod {p2} = {shared_b2}")
    print()
    
    if shared_a2 == shared_b2:
        print(f"   Shared secret key: {shared_a2}")
    else:
        print(f"   ✗ Keys don't match! Alice: {shared_a2}, Bob: {shared_b2}")
    
    # Check if it's a fixed point
    test_vals = [pow(12, i, 33) for i in range(1, 5)]
    if len(set(test_vals)) == 1:
        print(f"\n   Analysis: 12 is a fixed point (12^n ≡ 12 mod 33 for all n ≥ 1)")
        print(f"   This makes the function weak for cryptographic use.")
    
    # Problem 3.2
    print("\n3.2. Can we use 2^-1 (mod 6) as a common function?")
    print("-" * 40)
    
    inv = mod_inverse(2, 6)
    g_val = gcd(2, 6)
    
    print(f"   Checking: 2^-1 mod 6")
    print(f"   gcd(2, 6) = {g_val}")
    print()
    
    if inv is None:
        print(f"   Answer: NO")
        print(f"   Reason 1: The modular inverse doesn't exist because gcd(2, 6) ≠ 1")
        print(f"   Reason 2: Even if it existed, 2^-1 mod 6 is a constant, not a function")
        print(f"   Reason 3: For Diffie-Hellman we need g^x mod p, not a fixed value")
        print(f"   Reason 4: Modulus 6 is too small and not prime")
    else:
        print(f"   2^-1 mod 6 = {inv}")
        print(f"   However, this is still NOT suitable because:")
        print(f"   - It's a constant, not a function of x")
        print(f"   - We need g^x mod p for variable x")


def main():
    """Main program."""
    print("=" * 70)
    print("ZKGRA - Laboratory Work No. 4")
    print("Modular Arithmetic and Asymmetric Encryption")
    print()
    print("Student: Maroš Bednár (xbednarm1@stuba.sk)")
    print("Date: October 21, 2025")
    print("=" * 70)
    
    exercise_1()
    exercise_2()
    exercise_3()
    
    print_header("All exercises completed!", "=")


if __name__ == "__main__":
    main()
