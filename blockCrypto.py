from itertools import combinations

import EnglishDetect
import Operations
import StreamConvert


class BlockCrypto:
    def __init__(self, data=''):
        self.data = data
        self.EScore = EnglishDetect.EnglishDetect()
        self.highCypher = ''

    # Inputting data outside of initialization
    def dataIn(self, data):
        self.data = data

    # Get function for data being worked
    def dataGet(self):
        return self.data

    #Stripping line ends from end of lines in self.data
    def stripNewLines(self):
        for index, lines in enumerate(self.data):
            self.data[index] = lines.rstrip('\n\r')

    #Adding a file to data that has multiple lines to test
    def MultiLineFile(self, datafile, encoding):
        self.dataFile = datafile
        f = open(self.dataFile, "rb")
        self.data = f.readlines()
        f.close()
        self.stripNewLines()
        for index, lines in enumerate(self.data):
            self.data[index] = StreamConvert.convertHandler(lines,encoding,'BIN')

    #Single Byte Xor data against a given cipher
    def singleByteXor(self, cipher, workingData=None):
        if workingData is None:
            workingData = self.data
        return Operations.xorAgainst(workingData, cipher)

    # Checking english test score, largely useless as it currently stands, as I could just call the one line
    def checkEnglishScore(self, test):
        return self.EScore.scoreCheck(test)

    # Iterated through all byte combinations to find the byte that when used to decrypt workingData -
    # best matches english letter frequency
    def singleByteXorIterate(self, workingData=None):
        if workingData is None:
            workingData = self.data
        highScore = -9999
        highCypher = 0
        for cypher in range(0, 255):
            decrypted = self.singleByteXor(cypher, workingData)
            score = self.checkEnglishScore(decrypted)
            if score > highScore:
                highScore = score
                highCypher = cypher
        self.highCypher += chr(highCypher)
        decrypted = self.singleByteXor(highCypher, workingData)
        return decrypted

    # Inputs a file and iterates through the file, each line being considered a different possible -
    # encoded string, then choosing the one that most matches english letter frequency
    def singleByteXorIterateFile(self, file, encoding=None):
        self.MultiLineFile(file, encoding)
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

    # Returns the cypher built in decryption functions, to see the cypher used
    def getcypher(self):
        return self.highCypher

    # Resetting the cypher, in the event you wanted to use this object multiple times
    def resetCypher(self):
        self.highCypher = ''

    # known key, decrypting with XOR against key
    def repeatingXORKeyKnown(self, key):
        decrypted = Operations.xor(self.data, key)
        return decrypted

    # Uses Hamming distance to locate the most likely key length in XOR encryptions
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
                    hammingSum += Operations.binaryHamming(workingData[startBlock * key:(startBlock + 1) * key],
                                                           workingData[endblock * key:(endblock + 1) * key])
                    compares += 1
            hammingSum = hammingSum / key / compares
            if hammingSum < minHamming:
                minHamming = hammingSum
                bestKey = key
        return bestKey

    # Detecting a repeating key XOR encryption with unknown key
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

    #Looks for identical blocks 16 bytes apart, returns true if found
    def AESInECBDetect(self, string):
        AESKeysize = 16
        rangeOf = range(0, len(string), AESKeysize)
        combinationList = combinations(zip(rangeOf, rangeOf[1:]), 2)
        return any(string[x1:x2] == string[y1:y2] for (x1, x2), (y1, y2) in combinationList)

    # Works to find 1 AES in ECB encrypted string in a given file
    def AESDetectFile(self, workingFile, encoding=None):
        self.MultiLineFile(workingFile, encoding)
        AESStringFound = ''
        found=0
        for teststring in self.data:
            if self.AESInECBDetect(teststring):
                found=1
                AESStringFound = teststring
        if found is 1:
            return StreamConvert.binToHex(AESStringFound)
        return 0
