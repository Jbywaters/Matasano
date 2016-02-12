
from Crypto.Cipher import AES


class AESstuff:
    def __init__(self, key, mode=1, iv=None):
        if iv is None:
            self.cipher = AES.new(key, mode)
        else:
            self.cipher = AES.new(key, mode,iv)
    def encrypt(self, data):
        return self.cipher.encrypt(data)

    def decrypt(self, data):
        return self.cipher.decrypt(data)
