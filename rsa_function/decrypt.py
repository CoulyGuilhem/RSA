import base64


def decode_from_base64(encoded_message):
    ascii_bytes = base64.b64decode(encoded_message)
    return ascii_bytes.decode('ascii')


def decrypt_blocks(blocks, d, n):
    return [pow(int(block), d, n) for block in blocks]


def ascii_blocks_to_text(blocks):
    numeric_string = ''.join(str(block) for block in blocks)
    ascii_chars = [chr(int(numeric_string[i:i + 3])) for i in range(0, len(numeric_string), 3)]
    return ''.join(ascii_chars).rstrip('\x00')


def decrypt_message(encrypted_message, d, n):
    numeric_string = decode_from_base64(encrypted_message)
    block_size = len(str(n))
    blocks = [numeric_string[i:i + block_size] for i in range(0, len(numeric_string), block_size)]
    decrypted_blocks = decrypt_blocks(blocks, d, n)
    return ascii_blocks_to_text(decrypted_blocks)
