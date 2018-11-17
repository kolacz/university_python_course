def zaszyfruj(tekst, klucz):
    res = ""
    for c in tekst:
        d = ord(c) ^ klucz
        res += chr(d)
    return res

def odszyfruj(szyfr, klucz):
    return zaszyfruj(szyfr, klucz)

print(odszyfruj(zaszyfruj('python',7),7))
