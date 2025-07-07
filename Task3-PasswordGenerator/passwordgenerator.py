import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        if length < 1:
            print("Password length must be at least 1.")
            return
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__== "__main__":
    main()