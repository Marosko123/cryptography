"""
Command-line interface for ZKGRA Lab Work 2.

This module provides a CLI for Polybius encoding/decoding, XOR operations,
entropy calculations, and testing with surnames.
"""
import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from polybius import encode as polybius_encode, decode as polybius_decode
from xor_utils import xor_chain, evaluate_expression
from entropy import entropy_equiprobable


def main():
    parser = argparse.ArgumentParser(
        description='ZKGRA Lab Work 2: Polybius Square, XOR, and Entropy',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --encode "ENCRYPT ME 2 DAY"
  %(prog)s --decode "15 32 13 36 51 34 42"
  %(prog)s --xor 1011 0110 0100
  %(prog)s --entropy 8
  %(prog)s --surname "BEDNÁR"
        """
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--encode', type=str, metavar='TEXT',
                       help='Encode text using Polybius square')
    group.add_argument('--decode', type=str, metavar='PAIRS',
                       help='Decode Polybius-encoded text')
    group.add_argument('--xor', nargs='+', metavar='BITSTRING',
                       help='XOR multiple bitstrings')
    group.add_argument('--entropy', type=int, metavar='N',
                       help='Calculate entropy for N equiprobable outcomes')
    group.add_argument('--surname', type=str, metavar='NAME',
                       help='Test surname encoding/decoding')
    
    args = parser.parse_args()
    
    if args.encode:
        pairs, concatenated = polybius_encode(args.encode)
        print("Input:", args.encode)
        print("Space-separated pairs:", pairs)
        print("Concatenated:", concatenated)
        
    elif args.decode:
        decoded = polybius_decode(args.decode)
        print("Input:", args.decode)
        print("Decoded:", decoded)
        
    elif args.xor:
        if len(args.xor) < 2:
            print("Error: At least 2 bitstrings required for XOR", file=sys.stderr)
            return 1
        
        try:
            result = xor_chain(*args.xor)
            print("Bitstrings:", ' XOR '.join(args.xor))
            print("Result:", result)
            
            # If exactly 3 bitstrings, also show a^b^c^a^b
            if len(args.xor) == 3:
                a, b, c = args.xor
                expr_result = evaluate_expression(a, b, c)
                print(f"\nExpression a⊕b⊕c⊕a⊕b = {expr_result}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
            
    elif args.entropy is not None:
        try:
            h = entropy_equiprobable(args.entropy)
            print(f"Entropy H({args.entropy}) = {h:.6f} bits")
            if h == int(h):
                print(f"            = {int(h)} bits (exact power of 2)")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
            
    elif args.surname:
        from polybius import normalize_text
        pairs, concatenated = polybius_encode(args.surname)
        decoded = polybius_decode(pairs)
        normalized_input = normalize_text(args.surname)
        
        print("Surname:", args.surname)
        print("Encoded (pairs):", pairs)
        print("Encoded (concat):", concatenated)
        print("Decoded:", decoded)
        print("Match:", "✓" if decoded.replace(' ', '') == normalized_input.replace(' ', '') else "✗")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
