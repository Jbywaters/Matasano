import EnglishDetect
import Operations
from itertools import  combinations
import FileConvert
import ssl

import StreamConvert


class BlockCrypto:
    def __init__(self, data=''):
        self.data = data
        self.modified = data
        self.EScore = EnglishDetect.EnglishDetect()
        self.highCypher = ''

    def dataIn(self, data):
        self.data = data

    def dataGet(self):
        return self.data

    def MultiLineFile(self, datafile,encoding):
        self.dataFile = datafile
        f = open(self.dataFile, "rb")
        self.data = f.readlines()
        f.close()
        for index,lines in enumerate(self.data):
            self.data[index] = lines.rstrip('\n')
        if encoding is 'HEX':
            self.fileDecodeHex()
        elif encoding is 'B64':
            self.fileDecodeB64()
    def fileDecodeHex(self):
        for index,lines in enumerate(self.data):
            self.data[index] = StreamConvert.hexToBinary(lines)
    def fileDecodeB64(self):
        for index,lines in enumerate(self.data):
            self.data[index] = StreamConvert.b64ToBinary(lines)
    def singleByteXor(self, cipher, workingData=None):
        if workingData is None:
            workingData = self.data
        return Operations.xorAgainst(workingData, cipher)

    def checkEnglishScore(self, test):
        return self.EScore.scoreCheck(test)

    def singleByteXorIterate(self, workingData=None):
        if workingData is None:
            workingData = self.data
        highScore = -9999
        highCypher = 0
        for cypher in range(0, 255):
            testcypher = chr(cypher)
            decrypted = self.singleByteXor(cypher, workingData)
            score = self.checkEnglishScore(decrypted)
            if score > highScore:
                highScore = score
                highCypher=cypher
        self.highCypher += chr(highCypher)
        decrypted = self.singleByteXor(highCypher, workingData)
        return decrypted

    def singleByteXorIterateFile(self,file,encoding=None):
        self.MultiLineFile(file,encoding)
        highScore = -9999
        bestLine = 0
        for cypher in range(0, 255):
            for index, line in enumerate(self.data):
                score = self.checkEnglishScore(self.singleByteXor(cypher, line))
                if score > highScore:
                    highScore = score
                    self.highCypher = cypher
                    bestLine = index
        self.dataIn(self.data[bestLine])
        decrypted = self.singleByteXor(self.highCypher)
        return decrypted

    def getcypher(self):
        return self.highCypher
    def resetCypher(self):
        self.highCypher=''
    def repeatingKeyKnown(self, key):
        self.modified = Operations.xor(self.data, key)
        return self.modified

    def findKeySize(self, workingData=None, keymin=2, keymax=40):
        if workingData is None:
            workingData = self.data
        minHamming = 99999
        bestKey = 0
        for key in range(keymin, keymax):
            hammingSum = float(0)
            compares = 0
            for endblock in range(1, 4):
                for startBlock in range(0, endblock - 1):
                    hammingSum += Operations.binaryHamming(workingData[startBlock * key:(startBlock + 1) * key], workingData[endblock * key:(endblock + 1) * key])
                    compares+=1
            hammingSum = hammingSum /key/compares
            if hammingSum < minHamming:
                minHamming = hammingSum
                bestKey = key
        return bestKey

    def repeatingKeyUnknown(self, workingData=None):
        if workingData is None:
            workingData = self.data
        keysize = self.findKeySize(workingData)
        keyblocks = [''] * keysize
        for index, char in enumerate(workingData):
            keyblocks[index % keysize] += char
        for index, block in enumerate(keyblocks):
            keyblocks[index] = self.singleByteXorIterate(block)
        decrypted = ''
        for index in range(0, len(workingData)):
            decrypted += keyblocks[index % keysize][index / keysize]
        return decrypted
    def AESDetect(self,string):
        AESKeysize = 16
        rangeOf = range(0,len(string),AESKeysize)
        combinationList = combinations(zip(rangeOf,rangeOf[1:]),2)
        return any(string[x1:x2] == string[y1:y2] for (x1,x2), (y1,y2) in combinationList)

    def AESDetectFile(self,file,encoding=None):
        self.MultiLineFile(file,encoding)
        scoreMax = 99999
        aesPossible = ''
        for teststring in self.data:
            if self.AESDetect(teststring):
                print 'AES Found'
                aesPossible = teststring
        return StreamConvert.binToHex(aesPossible)