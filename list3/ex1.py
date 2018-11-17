def pierwsze_skladana(n):
    xs = range(2,n+1)
    t2 = [x for x in xs if all(x % y != 0 for y in range(2, int(x ** 0.5)+1))]
    return t2

def pierwsze_funkcyjna(n):
    return list(filter(lambda x: all(x % y != 0 for y in range(2, int(x ** 0.5)+ 1)), range(2,n+1) ))