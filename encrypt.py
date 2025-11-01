from cryptography.fernet import Fernet

def encrypt_string(plain_text: str) -> tuple[bytes, bytes]:
    key = Fernet.generate_key()
    cipher = Fernet(key)
    plain_text_bytes = plain_text.encode('utf-8')
    encrypted_blob = cipher.encrypt(plain_text_bytes)
    return encrypted_blob, key

sent_data, key = encrypt_string("Hello, World!")
print("Encrypted Data:", sent_data)
print("Encryption Key:", key)