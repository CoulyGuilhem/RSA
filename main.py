from rsa_function.rsa import key_gen, encrypt, decrypt


for i in range(10):
    print("=== Génération des clés RSA ===")
    (n_public, e), (n_private, d) = key_gen()

    print(f"Clé publique (n, e): ({n_public}, {e})")
    print(f"Clé privée (n, d): ({n_private}, {d})")

    message = "mon message"
    print("\n=== Message original ===")
    print(message)

    print("\n=== Chiffrement ===")
    encrypted = encrypt(message, e, n_public)
    print("Message chiffré :", encrypted)

    print("\n=== Déchiffrement ===")
    decrypted = decrypt(encrypted, d, n_private)
    print("Message déchiffré :", decrypted)

long_sequence = []

