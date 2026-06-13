import random
import string

while True:
    length = int(input("Enter password length (16-64): "))

    if 16 <= length <= 64:
        break

    print("Password length must be between 16 and 64.")

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)
