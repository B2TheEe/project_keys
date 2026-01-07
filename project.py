import base64
import os
import json
import hashlib
import binascii
from pathlib import Path
USERS_FILE = Path("users.json")

def load_users():
    if USERS_FILE.exists():
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def hash_password(password: str, salt: bytes, iterations: int = 200_000) -> str:
    dk = hashlib.pbkdf2_hmac(
        hash_name='sha256',
        password=base64.b64encode(password.encode('utf-8')),
        salt=salt,
        iterations=iterations,
    )
    return dk.hex()

def register_user():
    users = load_users()

    username = input("Kies een gebruikersnaam: ")
    if username in users:
        print("Gebruiker bestaat al.")
        return
    password = input("Kies een wachtwoord: ")

    # Genereer een salt van 16 bytes (aanbevolen voor PBKDF2)
    salt = binascii.hexlify(os.urandom(16)).decode('utf-8')
    print(f"Generated salt: {salt}")
    bytes_data = binascii.unhexlify(salt)
    hex_representation = bytes_data.hex()

    iterations = 100000  # Aanbevolen voor PBKDF2 in 2026
    print(f"Iterations: {iterations}")

    derived_key = (hash_password(password, bytes_data, iterations))

    users[username] = {
        "type": "user",
        "name": username,
        "roles": ["studenten"],
        "password_scheme": "pbkdf2",
        "pbkdf2_prf": "sha256",
        "salt": hex_representation,
        "iterations": iterations,
        "derived_key": derived_key,
        "encrypted_note": None
    }

    save_users(users)
    print("Gebruiker geregistreerd.")
def login():
    users = load_users()

    username = input("Gebruikersnaam: ")
    password = input("Wachtwoord: ")

    user = users.get(username)
    if not user:
        print("Onbekende gebruiker.")
        return None

    salt = bytes.fromhex(user["salt"])
    iterations = user["iterations"]
    derived_key = user["derived_key"]

    check = hash_password(password, salt, iterations)

    if check == derived_key:
        print("Login geslaagd.")
        return username
    else:
        print("Onjuist wachtwoord.")
        return None
def switch_menu():

    option = input("Choose one option: register OR login")
    match option:
        case "register":
            print("Gebruiker heeft het registeren van een gebruiker gekozen.")
            register_user()
        case "login":
            print("Gebruiker heeft inloggen gekozen")
            login()
        case _:
            print("Something's wrong with the internet")

def main():
    switch_menu()


if __name__ == "__main__":
    main()