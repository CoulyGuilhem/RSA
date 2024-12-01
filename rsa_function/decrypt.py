import base64


def decrypt_message(encrypted_message, d, n):
    decoded_message = base64.b64decode(encrypted_message).decode('ascii').replace(" ","")
    block_size = len(str(n))
    blocks = [decoded_message[i:i+block_size] for i in range(0, len(decoded_message), block_size)]
    decrypted_blocks = []
    for block in blocks:
        c = int(block)
        b = pow(c, d, n)
        decrypted_blocks.append(str(b).zfill(block_size - 1))
    numeric_string = ''.join(decrypted_blocks)
    numeric_string = numeric_string.lstrip('0')
    ascii_chars = [chr(int(numeric_string[i:i + 3])) for i in range(0, len(str(numeric_string)), 3)]
    plaintext = ''.join(ascii_chars).rstrip('\x00')
    return plaintext