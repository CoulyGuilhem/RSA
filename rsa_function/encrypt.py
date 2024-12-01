import base64


def encrypt_message(message, e, n):
    ascii_representation = ''.join(f"{ord(char):03}" for char in message)
    block_size = len(str(n)) - 1
    blocks = [ascii_representation[max(0, len(ascii_representation) - (i + block_size)):len(ascii_representation) - i] for i in range(0, len(ascii_representation), block_size)]
    completed_blocks = [block.zfill(block_size) for block in reversed(blocks)]
    encrypted_blocks = []
    for block in completed_blocks:
        B = int(block)
        C = pow(B, e, n)
        encrypted_blocks.append(str(C).zfill(block_size + 1))
    concatenated_blocks = " ".join(encrypted_blocks)
    encrypted_message = base64.b64encode(concatenated_blocks.encode()).decode()
    return encrypted_message

