import hashlib, binascii

def main():
    password = "Welkom123"
    salt = bytes.fromhex("afdbb8ca8f8ab45ef73a95af6a77fbc8")
    iterations = 600000

    derived = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        iterations
    )

    print(derived.hex())


if __name__ == "__main__":
    main()