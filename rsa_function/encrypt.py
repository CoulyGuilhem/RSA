import base64


def text_to_ascii_blocks(message, block_size):
    ascii_representation = ''.join(f"{ord(char):03}" for char in message)
    blocks = [ascii_representation[i:i + block_size] for i in range(0, len(ascii_representation), block_size)]
    if len(blocks[-1]) < block_size:
        blocks[-1] = blocks[-1].ljust(block_size, '0')
    return blocks


def encrypt_blocks(blocks, e, n):
    encrypted_blocks = [pow(int(block), e, n) for block in blocks]
    return encrypted_blocks


def encode_to_base64(encrypted_blocks):
    numeric_string = ''.join(f"{block:0{len(str(max(encrypted_blocks)))}d}" for block in encrypted_blocks)
    byte_representation = numeric_string.encode('ascii')
    return base64.b64encode(byte_representation).decode('ascii')


def encrypt_message(message, e, n):
    block_size = len(str(n)) - 1
    ascii_blocks = text_to_ascii_blocks(message, block_size)
    encrypted_blocks = encrypt_blocks(ascii_blocks, e, n)
    return encode_to_base64(encrypted_blocks)
