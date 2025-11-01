from cryptography.fernet import Fernet
from encrypt import encrypt_string

def decrypt_string(encrypted_blob: bytes, key: bytes) -> str:
    cipher = Fernet(key)
    decrypted_bytes = cipher.decrypt(encrypted_blob)
    return decrypted_bytes.decode('utf-8')

blob, key = encrypt_string("Hello, World!")
decrypted_text = decrypt_string(blob, key)
print("Decrypted Text:", decrypted_text)