from src.rsa import (
    euler_function, print_calculation_steps, 
    get_all_public_keys, encrypt_text, decrypt_text
)


def print_section(title):
    print(f"\n{'='*80}")
    print(f"{title}")
    print(f"{'='*80}")


def task_1():
    print_section("Task 1: Encrypt 'Bratislava' with p=5, q=7 (Private Key)")
    
    text = "Bratislava"
    p = 5
    q = 7
    
    print("\nNote: n=35 is too small for standard ASCII. Results may vary.")
    
    encrypted, e, n, d, decrypted = print_calculation_steps(text, p, q, key_type='private')
    
    print(f"\nResult:")
    print(f"Cryptogram: {encrypted}")
    print(f"Decrypted: {decrypted}")


def task_2():
    print_section("Task 2: Encrypt 'BANK' with p=9, q=11 (Public Key)")
    
    text = "BANK"
    p = 9
    q = 11
    
    print("\nNote: p=9 is not prime. For valid RSA, using p=7")
    p = 7
    
    encrypted, e, n, d, decrypted = print_calculation_steps(text, p, q, key_type='public')
    
    print(f"\nResult:")
    print(f"Cryptogram: {encrypted}")
    print(f"Decrypted: {decrypted}")


def task_3():
    print_section("Task 3: All Possible Public Keys")
    
    print("\n3.1. All possible public keys for p=7, q=11:")
    p1, q1 = 7, 11
    n1 = p1 * q1
    phi1 = euler_function(p1, q1)
    
    print(f"n = {p1} * {q1} = {n1}")
    print(f"φ(n) = ({p1}-1)({q1}-1) = {phi1}")
    
    public_keys_1 = get_all_public_keys(p1, q1)
    print(f"\nTotal possible public keys: {len(public_keys_1)}")
    print("\nPublic keys (e, n):")
    for i, (e, n) in enumerate(public_keys_1[:20], 1):
        print(f"{i:2d}. (e={e:2d}, n={n})")
    
    if len(public_keys_1) > 20:
        print(f"... and {len(public_keys_1) - 20} more")
    
    print("\n" + "-"*80)
    
    print("\n3.2. All possible public keys for p=9, q=11:")
    print("Note: p=9 is not prime. Using p=7 for valid RSA.")
    p2, q2 = 7, 11
    n2 = p2 * q2
    phi2 = euler_function(p2, q2)
    
    print(f"n = {p2} * {q2} = {n2}")
    print(f"φ(n) = ({p2}-1)({q2}-1) = {phi2}")
    
    public_keys_2 = get_all_public_keys(p2, q2)
    print(f"\nTotal possible public keys: {len(public_keys_2)}")
    print("\nPublic keys (e, n):")
    for i, (e, n) in enumerate(public_keys_2[:20], 1):
        print(f"{i:2d}. (e={e:2d}, n={n})")
    
    if len(public_keys_2) > 20:
        print(f"... and {len(public_keys_2) - 20} more")


def main():
    print("\n" + "="*80)
    print("Lab 8 - RSA Algorithm")
    print("="*80)
    
    task_1()
    task_2()
    task_3()
    
    print("\n" + "="*80)
    print("Done")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
