from .rijndael_tables import S_BOX, INV_S_BOX


def sub_bytes(state):
    return [S_BOX[byte] for byte in state]


def inv_sub_bytes(state):
    return [INV_S_BOX[byte] for byte in state]


def shift_rows(state):
    matrix = [[state[i + 4*j] for j in range(4)] for i in range(4)]
    
    for i in range(4):
        matrix[i] = matrix[i][i:] + matrix[i][:i]
    
    return [matrix[i][j] for j in range(4) for i in range(4)]


def inv_shift_rows(state):
    matrix = [[state[i + 4*j] for j in range(4)] for i in range(4)]
    
    for i in range(4):
        shift_amount = (4 - i) % 4
        matrix[i] = matrix[i][shift_amount:] + matrix[i][:shift_amount]
    
    return [matrix[i][j] for j in range(4) for i in range(4)]


def get_key_schedule_byte_order(key_length_bytes):
    return list(range(key_length_bytes))


def encode_message_hex(name):
    return ''.join(f'{ord(c):02x}' for c in name)


def encode_message_bytes(name):
    return [ord(c) for c in name]


def replace_bytes_in_data(data, replacements):
    result = []
    for byte in data:
        if byte in replacements:
            result.append(replacements[byte])
        else:
            result.append(S_BOX[byte])
    return result


def get_decimal_values(hex_values):
    result = []
    for val in hex_values:
        if isinstance(val, str):
            result.append(int(val, 16))
        else:
            result.append(val)
    return result
