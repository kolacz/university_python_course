from functools import reduce

def doskonale_skladana(n):
    xs = range(1,n+1)
    return [x for x in xs if x == sum([y for y in range(1,int(x/2)+1) if x % y == 0]) ]

def doskonale_funkcyjna(n):
    return list( filter(lambda x: x == reduce(lambda a,b : a+b, filter(lambda z: x % z == 0, range(1, int(x/2)+1)) , 0) , range(1,n+1)) )