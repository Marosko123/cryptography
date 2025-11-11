from src.rijndael import (
    sub_bytes, inv_sub_bytes, shift_rows, inv_shift_rows,
    encode_message_hex, encode_message_bytes, get_decimal_values,
    get_key_schedule_byte_order
)


def print_section(title):
    print(f"\n{'='*70}")
    print(f"{title}")
    print(f"{'='*70}")


def exercise_1():
    print_section("Exercise 1: SubBytes Transformations")
    
    name = "Maros Bednar"
    print(f"\nMessage M: {name}")
    
    hex_encoded = encode_message_hex(name)
    print(f"HEX format: {hex_encoded}")
    
    bytes_encoded = encode_message_bytes(name)
    print(f"ASCII bytes: {bytes_encoded}")
    print(f"HEX bytes: {[f'{b:02x}' for b in bytes_encoded]}")
    
    encrypted_bytes = sub_bytes(bytes_encoded)
    print(f"\nAfter S-box substitution:")
    print(f"DEC: {encrypted_bytes}")
    print(f"HEX: {[f'{b:02x}' for b in encrypted_bytes]}")


def exercise_2():
    print_section("Exercise 2: Decimal Notation")
    
    from src.rijndael_tables import S_BOX, INV_S_BOX
    
    # 2a
    forward_hex = ['01', 'ac', '03', '04', '64', '06', '0d', '10']
    forward_dec = get_decimal_values(forward_hex)
    
    print("\n2a) Forward substitution table:")
    print(f"HEX: {' '.join(forward_hex)}")
    print(f"DEC: {' '.join(str(d).rjust(2) for d in forward_dec)}")
    
    forward_vals = [S_BOX[d] for d in forward_dec]
    print(f"S-box (hex): {' '.join(f'{v:02x}' for v in forward_vals)}")
    print(f"S-box (dec): {' '.join(str(v).rjust(2) for v in forward_vals)}")
    
    # 2b
    inverse_hex = ['f1', 'f3', 'f4', 'f6', 'f8', 'ff', '10']
    inverse_dec = get_decimal_values(inverse_hex)
    
    print("\n2b) Inverse permutation table:")
    print(f"HEX: {' '.join(inverse_hex)}")
    print(f"DEC: {' '.join(str(d).rjust(3) for d in inverse_dec)}")
    
    inverse_vals = [INV_S_BOX[d] for d in inverse_dec]
    print(f"Inv S-box (hex): {' '.join(f'{v:02x}' for v in inverse_vals)}")
    print(f"Inv S-box (dec): {' '.join(str(v).rjust(3) for v in inverse_vals)}")


def exercise_3():
    print_section("Exercise 3: ShiftRows Operation")
    
    data_block = [
        0x63, 0x7c, 0x77, 0x7b,
        0xca, 0x82, 0xc9, 0x7d,
        0xb7, 0xfd, 0x93, 0x26,
        0x04, 0xc7, 0x23, 0xc3
    ]
    
    print("\nOriginal block:")
    print_data_block(data_block)
    
    shifted_block = shift_rows(data_block)
    
    print("\nAfter ShiftRows:")
    print_data_block(shifted_block)


def exercise_4():
    print_section("Exercise 4: Inverse Transformation")
    
    data_block = [
        0x63, 0x7c, 0x77, 0x7b,
        0xca, 0x82, 0xc9, 0x7d,
        0xb7, 0xfd, 0x93, 0x26,
        0x04, 0xc7, 0x23, 0xc3
    ]
    
    shifted_block = shift_rows(data_block)
    
    print("\nShifted block (from ex. 3):")
    print_data_block(shifted_block)
    
    inv_shifted_block = inv_shift_rows(shifted_block)
    
    print("\nAfter Inverse ShiftRows:")
    print_data_block(inv_shifted_block)
    
    if inv_shifted_block == data_block:
        print("\nVerification: OK - restored to original")
    else:
        print("\nError: mismatch!")


def exercise_5():
    print_section("Exercise 5: Byte Order Table")
    
    key_length = 160
    
    print(f"\nKey length: {key_length} bytes")
    
    byte_order = get_key_schedule_byte_order(key_length)
    
    print(f"\nByte order (0 to {key_length-1}):")
    
    for i in range(0, key_length, 16):
        row = byte_order[i:i+16]
        print(f"{i:3d}-{min(i+15, key_length-1):3d}: {' '.join(f'{b:3d}' for b in row)}")
    
    print(f"\nTotal: {len(byte_order)} bytes")


def print_data_block(block):
    print("\n4x4 matrix:")
    for i in range(4):
        row = [block[i + 4*j] for j in range(4)]
        print(f"  {' '.join(f'{b:02x}' for b in row)}")
    
    print(f"\nFlat: {' '.join(f'{b:02x}' for b in block)}")
    print(f"Dec:  {block}")


def main():
    print("\n" + "="*70)
    print("Lab 7 - Rijndael Algorithm")
    print("="*70)
    
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    
    print("\n" + "="*70)
    print("Done")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
