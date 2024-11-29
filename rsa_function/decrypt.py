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
    decoded_message = base64.b64decode(encrypted_message).decode('ascii')
    blocks = decoded_message.split(" ")
    decrypted_blocks = [str(pow(int(block), d, n)) for block in blocks]
    expected_block_length = len(str(n)) - 1
    normalized_blocks = [block.zfill(expected_block_length) for block in decrypted_blocks]
    numeric_string = ''.join(normalized_blocks)
    ascii_chars = [chr(int(numeric_string[i:i + 3])) for i in range(0, len(numeric_string), 3)]
    plaintext = ''.join(ascii_chars).rstrip('\x00')
    return plaintext
