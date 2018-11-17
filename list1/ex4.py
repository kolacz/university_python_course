def rozklad(n):
    i = 2
    res=[]
    while i <= n:
        ile = 0
        while (n%i==0):
            ile+=1
            n/=i
        if(ile > 0):
            res+=[(i,ile)]
        i+=1
    return res