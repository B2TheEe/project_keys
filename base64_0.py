import base64

def main():

    text = "Ethical hacking"
    # Encoderen
    encoded = base64.b64encode(text.encode())
    print("Base64 encoded:", encoded)
    # Decoderen
    decoded = base64.b64decode(encoded)
    print("Decoded:", decoded.decode())

    text.encode()
    #Zet de  tekst om in bytes.
    base64.b64encode(text)


if __name__ == "__main__":
    main()