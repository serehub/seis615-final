from cryptography.fernet import Fernet

print('Enter a message to encrypt:')
x = input()

key = Fernet.generate_key()
print(key)

f = Fernet(key)

token = f.encrypt(bytes(x, 'utf-8'))

print(token)
