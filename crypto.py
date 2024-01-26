from cryptography.fernet import Fernet
import base64

static_key = b'your_static_key_here'

encoded_key = base64.urlsafe_b64encode(static_key.ljust(32, b'\0')[:32])


def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message


if __name__ == "__main__":
    message_to_encrypt = "Hello, this is a secret message!"

    encrypted_message = encrypt_message(message_to_encrypt, encoded_key)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt_message(encrypted_message, encoded_key)
    print(f"Decrypted Message: {decrypted_message}")
