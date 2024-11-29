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
    # Décodage Base64
    decoded_message = base64.b64decode(encrypted_message).decode('ascii')
    print(f"Message décodé après Base64 : {decoded_message}")

    # Extraction des blocs chiffrés
    blocks = decoded_message.split(" ")
    print(f"Blocs chiffrés : {blocks}")

    # Déchiffrement des blocs
    decrypted_blocks = [str(pow(int(block), d, n)) for block in blocks]
    print(f"Blocs déchiffrés avant normalisation : {decrypted_blocks}")

    # Déterminer la longueur attendue des blocs
    expected_block_length = len(str(n)) - 1
    print(f"Longueur attendue des blocs déchiffrés : {expected_block_length}")

    # Normaliser la longueur des blocs en ajoutant des zéros au début si nécessaire
    normalized_blocks = [block.zfill(expected_block_length) for block in decrypted_blocks]
    print(f"Blocs déchiffrés normalisés : {normalized_blocks}")

    # Reconstruction du message ASCII
    numeric_string = ''.join(normalized_blocks)
    ascii_chars = [chr(int(numeric_string[i:i + 3])) for i in range(0, len(numeric_string), 3)]
    plaintext = ''.join(ascii_chars).rstrip('\x00')
    return plaintext
