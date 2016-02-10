import sys, os, sys, getopt, FileConvert,StreamConvert,Operations,binascii,blockCrypto
def tobinary(arg):
    return ' '.join(map(bin,bytearray(arg)))

def main():
    #Challenge 1
    challenge1 = StreamConvert.StreamConvert('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
    challenge1.hexToB64()
    print challenge1.getContent()
    #print binascii.a2b_base64(challenge1.getStream()) #To see words in result

    #Challenge 2
    challenge2a = StreamConvert.StreamConvert('1c0111001f010100061a024b53535009181c')
    challenge2a.hexToBinary()
    challenge2b = StreamConvert.StreamConvert('686974207468652062756c6c277320657965')
    challenge2b.hexToBinary()
    challenge2 = StreamConvert.binToHex(Operations.xor(challenge2a.getContent(), challenge2b.getContent()))
    print challenge2
    #print binascii.a2b_hex(xord) #To see words in result

    #Challenge 3
    challenge3 = blockCrypto.BlockCrypto(StreamConvert.hexToBinary('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))
    print challenge3.singleByteXorIterate()

    #challenge 4
    C4File = FileConvert.FileConvert('4.txt')
    C4File.hexToBinary()
    C4File.writeConverted('4converted.txt')
    challenge4 = blockCrypto.BlockCrypto('')
    challenge4.dataInFile('4converted.txt')
    print challenge4.singleByteXorIterateFile()

    #challenge 5
    challenge5 = blockCrypto.BlockCrypto("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
    print StreamConvert.binToHex(challenge5.repeatingKeyKnown('ICE'))

if __name__ == '__main__':
    main()
