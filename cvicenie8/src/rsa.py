import math


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y


def mod_inverse(e, phi):
    gcd_val, x, _ = extended_gcd(e, phi)
    if gcd_val != 1:
        return None
    return x % phi


def euler_function(p, q):
    return (p - 1) * (q - 1)


def generate_keys(p, q):
    n = p * q
    phi = euler_function(p, q)
    
    possible_e = []
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            possible_e.append(e)
    
    keys = []
    for e in possible_e:
        d = mod_inverse(e, phi)
        if d:
            keys.append({
                'public': (e, n),
                'private': (d, n),
                'e': e,
                'd': d,
                'n': n,
                'phi': phi
            })
    
    return keys


def encrypt_char(char, e, n):
    m = ord(char)
    c = pow(m, e, n)
    return c


def decrypt_char(c, d, n):
    m = pow(c, d, n)
    return chr(m)


def encrypt_text(text, e, n):
    encrypted = []
    for char in text:
        c = encrypt_char(char, e, n)
        encrypted.append(c)
    return encrypted


def decrypt_text(encrypted, d, n):
    decrypted = ""
    for c in encrypted:
        char = decrypt_char(c, d, n)
        decrypted += char
    return decrypted


def get_all_public_keys(p, q):
    keys = generate_keys(p, q)
    public_keys = [(k['e'], k['n']) for k in keys]
    return public_keys


def print_calculation_steps(text, p, q, key_type='private'):
    print(f"\nText: {text}")
    print(f"p = {p}, q = {q}")
    
    n = p * q
    phi = euler_function(p, q)
    
    print(f"\n1. n = p * q = {p} * {q} = {n}")
    print(f"2. φ(n) = (p-1)(q-1) = {p-1} * {q-1} = {phi}")
    
    if key_type == 'private':
        print(f"\n3. Choose e where gcd(e, φ(n)) = 1")
        e = 2
        while gcd(e, phi) != 1:
            e += 1
        print(f"   e = {e}")
        
        print(f"\n4. Calculate d = e^(-1) mod φ(n)")
        d = mod_inverse(e, phi)
        print(f"   d = {d}")
        
        print(f"\n   Private key: (d={d}, n={n})")
        print(f"   Public key: (e={e}, n={n})")
        
        print(f"\n5. Encryption (private key):")
        encrypted = []
        for char in text:
            m = ord(char)
            c = pow(m, d, n)
            print(f"   '{char}' -> m={m} -> c = {m}^{d} mod {n} = {c}")
            encrypted.append(c)
        
        print(f"\n   Cryptogram: {encrypted}")
        
        print(f"\n6. Decryption (public key):")
        decrypted = ""
        for c in encrypted:
            m = pow(c, e, n)
            if 0 <= m <= 127:
                char = chr(m)
                print(f"   c={c} -> m = {c}^{e} mod {n} = {m} -> '{char}'")
                decrypted += char
            else:
                print(f"   c={c} -> m = {c}^{e} mod {n} = {m} (invalid)")
                decrypted += "?"
        
        return encrypted, e, n, d, decrypted
    else:
        print(f"\n3. Choose e where gcd(e, φ(n)) = 1")
        e = 2
        while gcd(e, phi) != 1:
            e += 1
        print(f"   e = {e}")
        
        print(f"\n4. Calculate d = e^(-1) mod φ(n)")
        d = mod_inverse(e, phi)
        print(f"   d = {d}")
        
        print(f"\n   Public key: (e={e}, n={n})")
        print(f"   Private key: (d={d}, n={n})")
        
        print(f"\n5. Encryption (public key):")
        encrypted = []
        for char in text:
            m = ord(char)
            c = pow(m, e, n)
            print(f"   '{char}' -> m={m} -> c = {m}^{e} mod {n} = {c}")
            encrypted.append(c)
        
        print(f"\n   Cryptogram: {encrypted}")
        
        print(f"\n6. Decryption (private key):")
        decrypted = ""
        for c in encrypted:
            m = pow(c, d, n)
            if 0 <= m <= 127:
                char = chr(m)
                print(f"   c={c} -> m = {c}^{d} mod {n} = {m} -> '{char}'")
                decrypted += char
            else:
                print(f"   c={c} -> m = {c}^{d} mod {n} = {m} (invalid)")
                decrypted += "?"
        
        return encrypted, e, n, d, decrypted
