import hashlib, os

def main():


    password = "Welkom123"
    salt = os.urandom(16)

    hash_pw = hashlib.sha256(salt + password.encode()).hexdigest()
    print("Salt:", salt.hex())
    print("Hash:", hash_pw)

if __name__ == "__main__":
    main()