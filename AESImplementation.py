from Crypto import Cipher.AES

class AESstuff:
        def __init__(self, key,mode=1,iv=None):
            self.cipher = Crypto.Cipher.AES.new(key, mode,iv)
        def encrypt(self,data):
            return self.cipher.encrypt(data)
        def decrypt(self,data):
            return self.cipher.decrypt(data)

