import AESImplementation
import FileConvert
import Operations
import StreamConvert
import binascii
import blockCrypto


def main():
    # Challenge 1
    challenge1 = StreamConvert.StreamConvert(
        '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
    challenge1.hexToB64()
    print 'Challenge 1 Results: \n'
    print challenge1.getContent()
    print 'Key Was: '+binascii.a2b_base64(challenge1.getContent()),  # To see words in result


    # Challenge 2
    print '\nChallenge 2 Results: \n'
    challenge2a = StreamConvert.StreamConvert('1c0111001f010100061a024b53535009181c')
    challenge2a.hexToBinary()
    challenge2b = StreamConvert.StreamConvert('686974207468652062756c6c277320657965')
    challenge2b.hexToBinary()
    Ch2Result = StreamConvert.binToHex(Operations.xor(challenge2a.getContent(), challenge2b.getContent()))
    print Ch2Result
    print 'Key Was: '+binascii.a2b_hex(Ch2Result)  # To see words in result

    # Challenge 3
    print '\nChallenge 3 Results: \n'
    challenge3 = blockCrypto.BlockCrypto(
        StreamConvert.hexToBinary('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))
    print challenge3.singleByteXorIterate()

    # challenge 4
    print '\nChallenge 4 Results: \n'
    challenge4 = blockCrypto.BlockCrypto('')
    print challenge4.singleByteXorIterateFile('4.txt', 'HEX')

    print '\nChallenge 5 Results: \n'
    # challenge 5
    challenge5 = blockCrypto.BlockCrypto("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
    print StreamConvert.binToHex(challenge5.repeatingXORKeyKnown('ICE'))

    print '\nChallenge 6 Results: \n'
    # challenge 6
    C6File = FileConvert.FileConvert('6.txt')
    C6File.b64ToBinary()
    C6File.integrate()
    challenge6 = blockCrypto.BlockCrypto()
    challenge6.dataIn(C6File.getContent())
    print challenge6.repeatingKeyUnknown()

    print '\nChallenge 7 Results: \n'
    # challenge 7
    C7File = FileConvert.FileConvert('7.txt')
    C7File.b64ToBinary()
    C7File.integrate()
    challenge7 = AESImplementation.AESstuff('YELLOW SUBMARINE')
    print challenge7.decrypt(C7File.getContent())

    print '\nChallenge 8 Results: \n'
    # challenge 8
    challenge8 = blockCrypto.BlockCrypto()
    print 'Found AES ECB String: '+challenge8.AESDetectFile('8.txt', 'HEX')


if __name__ == '__main__':
    main()
