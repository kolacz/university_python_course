class ListaLiczb:
    def __iter__(self):
        self.licznik = 0
        return self
    def __next__ (self):
        if self.licznik >= 10: 
            raise StopIteration
        self.licznik += 1
        return self.licznik

class IntIterator(object):
    def __init__ (self):
        self.licznik = 0
    def __next__ (self):
        wynik = self.licznik
        self.licznik += 1
        return wynik

class IntCollection(object):
    def __iter__ (self):
        return IntIterator()

suma = 0
for i in IntCollection():
    if suma + i >= 100: break
    suma += i

print(suma)

def power2():
    power = 1
    while True:
        yield power
        power = power * 2

it = power2()
for x in range(4):
    print(next(it))


class Kolekcja:
    def __init__ (self):
        self.data = [1,2,3]
    def __iter__(self):
        self.pointer = 0
        return self
    def __next__(self):
        if self.pointer < len(self.data):
            self.pointer += 1
            return self.data[self.pointer - 1]
        else :
            raise StopIteration

wek1 = wek2 = Kolekcja()
suma = 0
for x in wek1:
    for y in wek2:
        suma += x*y
        print(x,y,suma)
