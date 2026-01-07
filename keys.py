import hashlib

def main():
    text = "IkBenErKlaarMee!"

    sha = hashlib.sha256(text.encode()).hexdigest()
    md5 = hashlib.md5(text.encode()).hexdigest()

    print("SHA-256:", sha)
    print("MD5:", md5)

if __name__ == "__main__":
    main()