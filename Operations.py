from itertools import cycle,imap
import operator

def xor(arg1,arg2):
    return ''.join(chr(ord(a)^ord(b)) for a,b in zip(arg1,cycle(arg2)))
def xorAgainst(arg1,xor):
    return ''.join(chr(ord(a)^xor) for a in arg1)
def xorAgaintKey(arg1,key):
    return ''.join(chr(ord(a)^key) for a in arg1)
def hammingDistance(arg1,arg2):
    assert len(arg1) == len(arg2)
    return sum(imap(operator.ne, arg1, arg2))
def binaryHamming(arg1,arg2):
    arg1 = ''.join([bin(ord(letter))[2:].zfill(8) for letter in arg1])
    arg2 = ''.join([bin(ord(letter))[2:].zfill(8) for letter in arg2])
    assert len(arg1) == len(arg2)
    return sum(imap(operator.ne, arg1, arg2))