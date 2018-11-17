class Wyrazenie:
    pass
    #   self.zmienne = {}
        
class Stala(Wyrazenie):
    def __init__(self,n):
        self.n = n
    def oblicz(self,zmienne):
        return self.n    
    def __str__(self):
        return str(self.n)

class Zmienna(Wyrazenie):
    def __init__(self,name):
        self.name = name
    def oblicz(self,zmienne):
        try:
            return zmienne[self.name]
        except KeyError as e:
            print(e,'is not defined.')
    def __str__(self):
        return self.name
            
class Plus(Wyrazenie):
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def oblicz(self,zmienne):
        return self.e1.oblicz(zmienne) + self.e2.oblicz(zmienne)
    def __str__(self):
        return '(' + str(self.e1) + '+' + str(self.e2) + ')'

class Minus(Wyrazenie):
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def oblicz(self,zmienne):
        return self.e1.oblicz(zmienne) - self.e2.oblicz(zmienne)
    def __str__(self):
        return '(' + str(self.e1) + '-' + str(self.e2) + ')'

class Mul(Wyrazenie):
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def oblicz(self,zmienne):
        return self.e1.oblicz(zmienne) * self.e2.oblicz(zmienne)
    def __str__(self):
        return str(self.e1) + '*' + str(self.e2)

class Div(Wyrazenie):
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def oblicz(self,zmienne):
        try:
            return self.e1.oblicz(zmienne) / self.e2.oblicz(zmienne)
        except ZeroDivisionError as x:
            print(x)
    def __str__(self):
        return str(self.e1) + '/' + str(self.e2)

###############################

class Instrukcja:
    def __init__(self):
        pass

class Przypisanie(Instrukcja):
    def __init__(self,x,e):
        self.x = x
        self.e = e
    def wykonaj(self,zmienne):
        zmienne[self.x] = self.e.oblicz(zmienne)
    def __str__(self):
        return self.x + ' = ' + str(self.e)

class If(Instrukcja):
    def __init__(self,e,e1,e2):
        self.e = e
        self.e1 = e1
        self.e2 = e2
    def wykonaj(self,zmienne):
        if self.e.oblicz(zmienne) == 0:
            return self.e2.oblicz(zmienne)
        else:
            return self.e1.oblicz(zmienne)
    def __str__(self):
        return 'if ' + str(self.e) + ' then ' + str(self.e1) + ' else ' + str(self.e2)
            
class Petla(Instrukcja):
    def __init__(self,c,inst):
        self.c = c
        self.inst = inst
    def wykonaj(self,zmienne):
        d = self.c.oblicz(zmienne)
        while(d):
            self.inst.wykonaj(zmienne)
            d = self.c.oblicz(zmienne)
    def __str__(self):
        return 'while(' + str(self.c) + '): ' + str(self.inst)

print(Petla(Zmienna("x"),Przypisanie("x",Plus(Zmienna("x"),Stala(1)))))