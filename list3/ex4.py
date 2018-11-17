from functools import reduce

def zaprzyjaznione_skladana(n):
    xs = [sum([x for x in range(1, int(i/2) + 1) if i % x == 0 ]) for i in range (1, n+1)]
    return [(x, xs[x-1]) for x in range(1, n+1) if xs[x-1]-1 < n and x == xs[xs[x-1]-1] and x < xs[x-1] ] 
       #1. warunek - żeby nie wyskoczyło poza tablice
       #2. warunek - sedno
       #3. warunek - żeby nie wypisywał par (l.doskonala, l. doskonala) i nie powtarzał (x,y),(y,x)

def zaprzyjaznione_funkcyjna(n): 
    def pairs(x):
        return (x[0]<x[1])
    xs = list(map( lambda z: list(filter(lambda w: z % w == 0, range(1, int(z/2) + 1))) , range(1,n+1))) #lista list dzielników 
    ys = list(map( lambda y,z: (y,reduce(lambda x,y: x+y, z, 0)), range(1,n+1), xs))
    zs = list(map( lambda y: tuple(reversed(y)), ys))
    return list(filter(pairs,filter(lambda x: x in zs,ys)))

print( zaprzyjaznione_funkcyjna(10000) )
print( zaprzyjaznione_skladana(10000) )