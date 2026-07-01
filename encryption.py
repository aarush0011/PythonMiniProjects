import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#ENCRYPTION
plain_text = input("Enter you message: ")
cipher_text = ""

for letters in plain_text:
    index = chars.index(letters)
    cipher_text += key[index]

print(f"Encrypted message: {cipher_text}")

#DECRYPTION
cipher_text = input("Enter you Encrypted message: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"The message: {plain_text}")