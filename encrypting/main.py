import random
import string

char = string.whitespace + string.punctuation +string.digits + string.ascii_letters
char  = list(char)
key = char.copy()
random.shuffle(key)

print(char)
print(key)
plain_text = input("Enter text to encrypte: ")
cipher_text = ""

for letter in plain_text:
    index = char.index(letter)
    cipher_text +=key[index]
print(f'original text: {plain_text}')
print(f'encrypted text: {cipher_text}')


ciphers_text = input("Enter text to decrypte: ")
plains_text = ""

for letter in ciphers_text:
    index = key.index(letter)
    plains_text +=char[index]
print(f'original text: {ciphers_text}')
print(f'decrypted text: {plains_text}')