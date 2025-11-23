from src.hash_functions import get_parameters, hash_1, hash_2, custom_hash
from src.schnorr import Schnorr

def print_section(title):
    print(f"\n{'='*80}")
    print(f"{title}")
    print(f"{'='*80}")

def task_1():
    print_section("Task 1: Hash Functions with IP Tables")
    
    print(f"{'Case':<10} | {'n':<10} | {'m':<10} | {'h(n)=n%m':<15} | {'n1..n6':<30} | {'h(n)=sum(h(ni))%m':<20}")
    print("-" * 110)
    
    # 5 combinations
    for i in range(5):
        # Case A: even n, odd m
        try:
            n_a, m_a = get_parameters('even', 'odd')
            h1_a = hash_1(n_a, m_a)
            
            ns_a, _ = get_parameters('even', 'odd', count_n=6) # Parity of ni not specified, assuming same as n? 
            # "Combinations must be calculated for cases when: A) even n and odd m"
            # It doesn't explicitly say n1-n6 must be even. But usually "n" refers to the input.
            # Let's assume n1-n6 are chosen arbitrarily as per "chosen from the tables... arbitrarily".
            # But maybe the "even n" applies to the input of the hash function.
            # For 1.2, the input is effectively the sequence.
            # I will just pick random n1-n6 from tables without parity restriction for 1.2, 
            # or maybe follow the "even n" rule for all inputs. 
            # Let's assume "n" in "even n" refers to the single value in 1.1.
            # For 1.2, I'll just pick random values.
            
            # Actually, let's look at the text: "Combinations must be calculated for cases when: A) even n and odd m".
            # In 1.1, n is the input. In 1.2, n is not the input, n1..n6 are.
            # Maybe it means "even result of sum" or something?
            # Or maybe it means for 1.1 we use even n, odd m.
            # And for 1.2 we use... what?
            # I will assume the condition applies to the single n in 1.1.
            # For 1.2, I will use random n1-n6.
            
            # Re-reading: "Calculate hash functions... for each of the following tasks... 1.1... 1.2... Combinations must be calculated for cases when..."
            # This implies we need to do A and C for BOTH 1.1 and 1.2.
            # For 1.2, what is "n"? There is no "n" in the formula 1.2, only n1..n6.
            # Maybe "n" refers to the inputs n1..n6? i.e. all of them even?
            # Or maybe n is just a variable name used in the condition description.
            # I will assume for 1.2 that all n1..n6 should satisfy the parity condition of "n".
            
            ns_a, _ = get_parameters('even', 'odd', count_n=6) # Using m_a from above or new m? "Combinations of n and m".
            # I'll use the same m for 1.1 and 1.2 in this iteration for simplicity, or pick new.
            # Let's pick new to be safe/diverse.
            _, m_a2 = get_parameters('even', 'odd')
            
            h2_a = hash_2(ns_a, m_a2)
            
            print(f"{'A (e,o)':<10} | {n_a:<10} | {m_a:<10} | {h1_a:<15} | {str(ns_a):<30} | {h2_a:<20} (m={m_a2})")
            
        except Exception as e:
            print(f"Error in Case A: {e}")

        # Case C: odd n, even m
        try:
            n_c, m_c = get_parameters('odd', 'even')
            h1_c = hash_1(n_c, m_c)
            
            ns_c, _ = get_parameters('odd', 'even', count_n=6)
            _, m_c2 = get_parameters('odd', 'even')
            
            h2_c = hash_2(ns_c, m_c2)
            
            print(f"{'C (o,e)':<10} | {n_c:<10} | {m_c:<10} | {h1_c:<15} | {str(ns_c):<30} | {h2_c:<20} (m={m_c2})")
            
        except Exception as e:
            print(f"Error in Case C: {e}")
            
        print("-" * 110)

def task_2():
    print_section("Task 2: Custom Hash Algorithm")
    
    test_strings = [
        "Hello World",
        "Cryptography",
        "Slovak University of Technology",
        "A",
        "B"
    ]
    
    print(f"{'Input String':<40} | {'Hash Code (Hex)':<20}")
    print("-" * 60)
    
    for s in test_strings:
        h = custom_hash(s)
        print(f"{s:<40} | {h:<20}")

def task_3_4():
    print_section("Task 3 & 4: Schnorr Digital Signature")
    
    print("Initializing Schnorr parameters (generating primes, this might take a moment)...")
    # Using slightly larger primes for demonstration than minimal, but small enough to be fast
    schnorr = Schnorr() 
    
    print(f"Parameters:")
    print(f"p ({schnorr.p.bit_length()} bits) = {schnorr.p}")
    print(f"q ({schnorr.q.bit_length()} bits) = {schnorr.q}")
    print(f"g = {schnorr.g}")
    
    print("\n1. Key Generation:")
    x, y = schnorr.generate_keys()
    print(f"Private key x = {x}")
    print(f"Public key y = {y}")
    
    message = "This is a signed message."
    print(f"\n2. Signing message: '{message}'")
    e, s = schnorr.sign(message)
    print(f"Signature (e, s):")
    print(f"e = {e}")
    print(f"s = {s}")
    
    print("\n3. Verification:")
    is_valid = schnorr.verify(message, e, s, y)
    print(f"Signature valid? {is_valid}")
    
    print("\n4. Verification with wrong message:")
    is_valid_wrong = schnorr.verify("Tampered message", e, s, y)
    print(f"Signature valid for 'Tampered message'? {is_valid_wrong}")

def main():
    print("\n" + "="*80)
    print("Lab 9 - Hash Functions and Digital Signatures")
    print("="*80)
    
    task_1()
    task_2()
    task_3_4()
    
    print("\n" + "="*80)
    print("Done")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
