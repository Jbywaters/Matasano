import binascii
import re

class BadEncoding(Exception):
    def __init__(self,startEncoding,endEncoding):
        self.startEncoding = startEncoding
        self.endEncoding =endEncoding
    def __str__(self):
        return {self.startEncoding,self.endEncoding}

def convertHandler(stream, startEncoding, endEncoding):
    try:
        if startEncoding is 'HEX':
            if endEncoding is 'BIN':
                return hexToBinary(stream)
            elif endEncoding is 'B64':
                return hexToB64(stream)
        if startEncoding is 'B64':
            if endEncoding is 'BIN':
                return b64ToBinary(stream)
            elif endEncoding is 'HEX':
                return b64ToHex(stream)
        if startEncoding is 'BIN':
            if endEncoding is 'HEX':
                return binToHex(stream)
            elif endEncoding is 'B64':
                return binToB64(stream)
    except TypeError as e:
        print e
        print startEncoding+' TO '+endEncoding+' Failed'
        raise BadEncoding(startEncoding,endEncoding)

def detectEncoding(stream):
    b64Reg = '^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$'
    HEXReg = '^[0-9A-F]+$'
    BINReg = '^(1|0)+$'
    if re.match(b64Reg,stream):
        return 'B64'
    if re.match(HEXReg,stream):
        return 'HEX'
    if re.match(BINReg,stream):
        return 'BIN'
    else:
        return None

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
    stream = binascii.b2a_base64(stream).rstrip('\n')
    return stream


def b64ToHex(stream):
    stream = binascii.a2b_base64(stream)
    stream = binascii.b2a_hex(stream)
    return stream


def binToHex(stream):
    stream = binascii.b2a_hex(stream)
    return stream


def binToB64(stream):
    stream = binascii.b2a_base64(stream).rstrip('\n')
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
    stream = binascii.b2a_base64(stream).rstrip('\n')
    return stream


def binaryString(stream):
    return ''.join([bin(ord(letter))[2:].zfill(8) for letter in stream])


class StreamConvert:
    def __init__(self, stream=''):
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
        self.stream = binascii.b2a_base64(self.stream).rstrip('\n')
        return self.stream

    def b64ToHex(self):
        self.stream = binascii.a2b_base64(self.stream)
        self.stream = binascii.b2a_hex(self.stream)
        return self.stream

    def binToHex(self):
        self.stream = binascii.b2a_hex(self.stream)
        return self.stream

    def binToB64(self):
        self.stream = binascii.b2a_base64(self.stream).rstrip('\n')
        return self.stream

    def getContent(self):
        return self.stream
