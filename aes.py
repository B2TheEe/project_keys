from cryptography.fernet import Fernet



def main():
    # Stap 1: maak een AES-sleutel
    key = Fernet.generate_key()
    cipher = Fernet(key)

    # Stap 2: bericht
    message = b"Dit is geheim"

    # Stap 3: encrypt
    token = cipher.encrypt(message)
    print("Encrypted:", token)

    # Stap 4: decrypt
    plain = cipher.decrypt(token)
    print("Decrypted:", plain)







if __name__ == "__main__":
    main()