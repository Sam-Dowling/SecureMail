#!/usr/bin/env python3

import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class AES:
    def Set_Key(self, key):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(key.encode('utf-8'))
        self.cipher_suite = Fernet(base64.urlsafe_b64encode(digest.finalize()))

    def Encrypt(self, plaintext):
        return self.cipher_suite.encrypt(plaintext.encode('utf-8')).decode("utf-8")

    def Decrypt(self, ciphertext):
        return self.cipher_suite.decrypt(ciphertext.encode('utf-8')).decode("utf-8")

    def Encrypt_File(self, file):
        return self.cipher_suite.encrypt(read_file(file))

    def Decrypt_File(self, data, file):
        plaintext = base64_decode_safe(self.cipher_suite.decrypt(data))
        with open(file, 'w') as f:
            f.write(plaintext)

def base64_encode_safe(text):
    return base64.urlsafe_b64encode(text).decode("utf-8")

def base64_decode_safe(text):
    return base64.urlsafe_b64decode(text).decode("utf-8")

def read_file(path):
    with open(path, 'rb') as f:
        return base64_encode_safe(f.read())
