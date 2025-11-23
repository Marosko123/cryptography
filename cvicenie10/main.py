from src.redundant_code import get_non_redundant_codes, encode_redundant
from src.huffman import build_huffman_tree, generate_huffman_codes, print_huffman_table

def run_task_1():
    print("--- Task 1: Redundant Code (Parity Bit) ---")
    codes = get_non_redundant_codes()
    
    print(f"{'Symbol':<8} | {'Non-Redundant':<15} | {'Redundant (with parity)':<25}")
    print("-" * 55)
    
    for symbol, code in codes.items():
        redundant = encode_redundant(code)
        print(f"{symbol:<8} | {code:<15} | {redundant:<25}")
    print("\n")

def run_task_2():
    print("--- Task 2: Huffman Coding ---")
    # Arbitrary probabilities summing to 1
    probabilities = {
        'x1': 0.25,
        'x2': 0.20,
        'x3': 0.15,
        'x4': 0.15,
        'x5': 0.10,
        'x6': 0.10,
        'x7': 0.05
    }
    
    print("Input Probabilities:")
    for s, p in probabilities.items():
        print(f"{s}: {p}")
    print("")

    root = build_huffman_tree(probabilities)
    codes = generate_huffman_codes(root)
    
    print_huffman_table(probabilities, codes)

if __name__ == "__main__":
    run_task_1()
    run_task_2()
