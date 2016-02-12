import binascii
def hexToBinary(stream):
    stream = binascii.a2b_hex(stream)
    return stream
def hexToBinary(stream):
    stream = binascii.a2b_hex(stream)
    return stream
def b64ToBinary(stream):
    stream = binascii.a2b_base64(stream)
    return stream
def hexToB64(stream):
    stream = binascii.a2b_hex(stream)
    stream = binascii.b2a_base64(stream)
    return stream
def b64ToHex(stream):
    stream = binascii.a2b_base64(stream)
    stream = binascii.b2a_hex(stream)
    return stream
def binToHex(stream):
    stream = binascii.b2a_hex(stream)
    return stream
def binToB64(stream):
    stream = binascii.b2a_base64(stream)
    return stream
def ueToBin(stream):
    stream = binascii.a2b_qp(stream)
    return stream
def ueToHex(stream):
    stream = binascii.a2b_qp(stream)
    stream = binascii.b2a_hex(stream)
    return stream
def ueToB64(stream):
    stream = binascii.a2b_qp(stream)
    stream = binascii.b2a_base64(stream)
    return stream
def binaryString(stream):
        return ''.join([bin(ord(letter))[2:].zfill(8) for letter in stream])
class StreamConvert:
    def __init__(self,stream=''):
        self.stream = stream
    def hexToBinary(self):
        self.stream = binascii.a2b_hex(self.stream)
        return self.stream
    def hexToBinary(self):
        self.stream = binascii.a2b_hex(self.stream)
        return self.stream
    def b64ToBinary(self):
        self.stream = binascii.a2b_base64(self.stream)
        return self.stream
    def hexToB64(self):
        self.stream = binascii.a2b_hex(self.stream)
        self.stream = binascii.b2a_base64(self.stream)
        return self.stream
    def b64ToHex(self):
        self.stream = binascii.a2b_base64(self.stream)
        self.stream = binascii.b2a_hex(self.stream)
        return self.stream
    def binToHex(self):
        self.stream = binascii.b2a_hex(self.stream)
        return self.stream
    def binToB64(self):
        self.stream = binascii.b2a_base64(self.stream)
        return self.stream
    def getContent(self):
        return self.stream
