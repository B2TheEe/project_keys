import hashlib, os

def hash_password(password):
    salt = os.urandom(16)
    hashed = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt, hashed


def main():
    salt, pw_hash = hash_password("Welkom123")
    print("Salt:", salt.hex())
    print("Hash:", pw_hash)

if __name__ == "__main__":
    main()