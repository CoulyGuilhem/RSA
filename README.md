# RSA

Liste des commandes :

### Créer les clés SSH :
python monRSA.py keygen -s <key_size> -f <filename>

### Chiffrer un message :
python monRSA.py crypt <public_key_file> <message_or_input_file> [-i <input_file>] [-o <output_file>]

### Déchiffrer un message :
python monRSA.py decrypt <private_key_file> <encrypted_text_or_input_file> [-i <input_file>] [-o <output_file>]

### Obtenir de l'aide
python monRSA.py help
