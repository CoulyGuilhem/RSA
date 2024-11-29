import argparse
import base64
from rsa_function.rsa import key_gen, encrypt, decrypt


def write_key_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)


def read_key_file(filename):
    with open(filename, "r") as f:
        return f.readlines()


def process_key_file(key_file, is_public):
    try:
        lines = read_key_file(key_file)
        header = "---begin monRSA public key---" if is_public else "---begin monRSA private key---"
        if lines[0].strip() != header:
            raise ValueError("Invalid key file format.")
        encoded_key = lines[1].strip()
        decoded_key = base64.b64decode(encoded_key).decode("ascii")
        n_hex, key_hex = decoded_key.split("\n")
        n, key = int(n_hex, 16), int(key_hex, 16)
        return n, key
    except Exception as e:
        raise ValueError(f"Error reading key file: {e}")


def create_key_files(base_name="monRSA", size=10):
    (n_public, e), (n_private, d) = key_gen(size=size)
    pub_content = "---begin monRSA public key---\n" + base64.b64encode(
        (f"{n_public:x}\n{e:x}").encode()
    ).decode() + "\n---end monRSA key---"
    priv_content = "---begin monRSA private key---\n" + base64.b64encode(
        (f"{n_private:x}\n{d:x}").encode()
    ).decode() + "\n---end monRSA key---"

    write_key_file(f"{base_name}.pub", pub_content)
    write_key_file(f"{base_name}.priv", priv_content)
    print(f"Keys generated with size {size} digits: {base_name}.pub, {base_name}.priv")


def main():
    global result
    parser = argparse.ArgumentParser(
        description="RSA Encryption/Decryption Tool"
    )
    parser.add_argument("command", choices=["keygen", "crypt", "decrypt", "help"], help="Command to execute")
    parser.add_argument("key", nargs="?", help="Key file (public or private)")
    parser.add_argument("text", nargs="?", help="Text to encrypt or decrypt")
    parser.add_argument("-f", "--filename", default="monRSA", help="Base name for generated keys")
    parser.add_argument("-s", "--size", type=int, default=10, help="Size of keys to generate")
    parser.add_argument("-i", "--input", help="Input file for text")
    parser.add_argument("-o", "--output", help="Output file for results")

    args = parser.parse_args()

    if args.command == "help" or not args.command:
        parser.print_help()
        return

    if args.command == "keygen":
        create_key_files(base_name=args.filename, size=args.size)
    elif args.command in ["crypt", "decrypt"]:
        if not args.key:
            print("Error: Key file is required for crypt/decrypt.")
            return

        if args.input:
            try:
                with open(args.input, "r") as f:
                    text = f.read().strip()
            except FileNotFoundError:
                print(f"Error: File {args.input} not found.")
                return
        else:
            if not args.text:
                print("Error: Text is required when input file is not provided.")
                return
            text = args.text

        is_public_key = args.command == "crypt"
        try:
            n, key = process_key_file(args.key, is_public=is_public_key)
        except ValueError as e:
            print(f"Error: {e}")
            return

        try:
            if args.command == "crypt":
                result = encrypt(text, key, n)
            else:
                result = decrypt(text, key, n)
        except Exception as e:
            print(f"Error during {args.command}: {e}")
            return

        if args.output:
            with open(args.output, "w") as f:
                f.write(result)
            print(f"Output written to {args.output}")
        else:
            print(f"Result: {result}")
    else:
        print("Invalid command. Use 'help' to see usage.")


if __name__ == "__main__":
    main()
