import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password

# User input
length = int(input("Enter password length: "))

print("Generated Password:", generate_password(length))