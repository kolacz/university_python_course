from math import log

def is_prime(n):
    if(n == 0 or n == 1):
        return False
    res = True
    for i in range(2, int(n ** 0.5) + 1):
        if(n % i == 0):
            res = False
    return res

def rozklad_skladana(n):
    primes = [x for x in range(2,n+1) if is_prime(x)] # lista liczb pierwszych od 2 do n
    xs = [ x for x in primes for i in range(1, int(log(n,x))+1) if n % (x**i) == 0 ] # bo x wystąpi co najwyżej log(n,x) razy w rozkładzie n
    return list(sorted(set([(x,xs.count(x)) for x in xs]))) # kosmetycznie -> bo "set" ustawiał w odwrotnej kolejności

def rozklad_funkcyjna(n):
    def aux(i):
        return aux1(i,n,0)
    def aux1(i,n,acc):
        if(n % i == 0):
            return aux1(i,n/i,acc+1)
        else:
            return (i,acc)
    primes = list(filter(is_prime, range(2,n+1)))
    return list(map(aux,filter(lambda x: n % x == 0,primes)))


print ( rozklad_funkcyjna(111111) )
print ( rozklad_skladana(111111) )