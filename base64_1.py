import os
def main():

    random_bytes = os.urandom(16)
    print(random_bytes)

if __name__ == "__main__":
    main()