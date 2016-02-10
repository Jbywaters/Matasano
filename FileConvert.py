import binascii
class FileConvert:
    def __init__(self, file):
        self.file = file
        f = open(self.file, "rb")
        self.content = f.readlines()
        f.close()
        for index,lines in enumerate(self.content):
            self.content[index] = lines.rstrip('\n')
    def hexToB64(self):
        for index,lines in enumerate(self.content):
            self.content[index] = binascii.b2a_base64(lines)
    def hexToBinary(self):
        for index,lines in enumerate(self.content):
            self.content[index] = binascii.a2b_hex(lines)
    def hexToBinary(self):
        for index,lines in enumerate(self.content):
            self.content[index] = binascii.a2b_hex(lines)
    def b64ToBinary(self):
        for index,lines in enumerate(self.content):
            self.content[index] = binascii.a2b_base64(lines)
    def b64ToHex(self):
        for index,lines in enumerate(self.content):
            lines = binascii.a2b_base64(lines)
            self.content[index] = binascii.b2a_hex(lines)
    def binToHex(self):
        for index,lines in enumerate(self.content):
            self.content[index] = binascii.b2a_hex(lines)
    def binToB64(self):
        for index,lines in enumerate(self.content):
            self.content[index] = binascii.b2a_base64(lines)
    def getContent(self):
        return self.content
    def writeConverted(self,name):
        f = open(name, "wb")
        f.writelines("%s\n" % l for l in self.content) # Writelines is a lie, as it does not write a newline after each string
        f.close()