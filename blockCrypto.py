import EnglishDetect
import Operations


class BlockCrypto:
    def __init__(self, data):
        self.data = data
        self.modified = data
        self.EScore = EnglishDetect.EnglishDetect()
        self.highCypher = 0

    def dataIn(self, data):
        self.data = data

    def dataInFile(self, datafile):
        f = open(datafile, "rb")
        self.fileLines = f.readlines()
        f.close()

    def singleByteXor(self, cipher):
        self.modified = Operations.xorAgainst(self.data, cipher)

    def checkEnglishScore(self):
        return self.EScore.scoreCheck(self.modified)

    def singleByteXorIterate(self):
        highScore = 0;
        for cypher in range(0, 255):
            self.singleByteXor(cypher)
            score = self.checkEnglishScore()
            if score > highScore:
                highScore = score
                self.highCypher = cypher
        self.singleByteXor(self.highCypher)
        return self.modified

    def singleByteXorIterateFile(self):
        highScore = 0
        bestLine = 0
        topCypher = 0
        for cypher in range(0, 255):
            for index, line in enumerate(self.fileLines):
                self.dataIn(line)
                self.singleByteXor(cypher)
                score = self.checkEnglishScore()
                if score > highScore:
                    highScore = score
                    topCypher = cypher
                    bestLine = index
        self.dataIn(self.fileLines[bestLine])
        self.singleByteXor(topCypher)
        return self.modified

    def repeatingKeyKnown(self, key):
        self.modified = Operations.xor(self.data, key)
        return self.modified
