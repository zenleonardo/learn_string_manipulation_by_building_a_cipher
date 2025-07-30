# src/main.py
from cipher_logic import decrypt

text_to_decrypt = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

print(f'\nEncrypted text: {text_to_decrypt}')
print(f'Key: {custom_key}')

decryption = decrypt(text_to_decrypt, custom_key)

print(f'\nDecrypted text: {decryption}\n')