from functools import reduce
import time

def doskonale_skladana(n):
    xs = range(1,n+1)
    return [x for x in xs if x == sum([y for y in range(1,int(x/2)+1) if x % y == 0]) ]

def doskonale_funkcyjna(n):
    return list( filter(lambda x: x == reduce(lambda a,b : a+b, filter(lambda z: x % z == 0, range(1, int(x/2)+1)) , 0) , range(1,n+1)) )

def dzielniki(x,k):
    for i in range(1,k+1):
        if( x % i == 0 ):
            yield i

def doskonale(n):
    for i in range(1,n+1):
        suma = 0
        for k in dzielniki(i,int(i/2)):
            suma += k
        if(i == suma):
            yield i

def doskonale_iter(n):
    res=[]
    for i in doskonale(n):
        res.append([i])
    return res

ns = [1,10,100,1000,10000]

def times(n):
    res = []
    t0 = time.clock()
    doskonale_skladana(n)
    res.append('{:.6f}'.format(time.clock()-t0))

    t1 = time.clock()
    doskonale_funkcyjna(n)
    res.append('{:.6f}'.format(time.clock()-t1))

    t2 = time.clock()
    doskonale_iter(n)
    res.append('{:.6f}'.format(time.clock()-t2))
    return res

A = [ times(a) for a in ns ]

def test():
    d = len(ns)
    e = len(str(ns[d-1]))
    for i in range(e+1):
        print(" ", end="")
    print("składana funkcyjna iteracyjna")
    for i in range(d):
        print(str(ns[i]).ljust(e), end=" ")
        for j in range(3):
            print(str(A[i][j]).rjust(8+j), end=" ")
        print("")

test()

