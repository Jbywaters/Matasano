from itertools import cycle

def xor(arg1,arg2):
    return ''.join(chr(ord(a)^ord(b)) for a,b in zip(arg1,cycle(arg2)))
def xorAgainst(arg1,xor):
    return ''.join(chr(ord(a)^xor) for a in arg1)
def xorAgaintKey(arg1,key):
    return ''.join(chr(ord(a)^key) for a in arg1)