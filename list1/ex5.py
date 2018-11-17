def tabliczka(x1,x2,y1,y2):
    x = list(range(x1,x2+1))
    
    # wypisywanie spacji w górnym lewym rogu
    space = len(str(y2))
    for i in range(space+1):
        print(" ", end="")
    
    # wyliczanie długości liczb w ostatnim wierszu,
    # dzięki którym będzie możliwe rozsądnie wyrównanie
    sizes = [len(str(k*y2)) for k in x]

    # wypisanie pierwszego wiersza
    for i in range(x2-x1+1):
        print(str(x[i]).ljust(sizes[i]), end=" ")
    print("")

    # wypisanie kolejnych wierszy
    for i in range(y1,y2+1): # range na przedziale
        print(str(i).ljust(space), end=" ")
        for j in range(x2-x1+1): # range od liczby
            print(str(x[j]*i).ljust(sizes[j]), end=" ")      
        print("")  
            
        