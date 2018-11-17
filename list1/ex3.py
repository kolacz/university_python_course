def slownie(n):
    res=[]
    i = 0
    x = list(reversed (str(n))) # 1234 -> ['4','3','2','1']
    length = len(x)
    
    while i < length:
        j = int(x[i])
        if (i+1 < length):
            d = int(x[i+1])
        else:
            d = 0
        if (i+2 < length):
            s = int(x[i+2])
        else:
            s = 0

        if (i == 3):
            if  (s == 0) and (d == 0) and (j == 1):
                res+=["tysiąc"]
            elif(j >= 2) and (j <= 4):
                if (d == 1):
                    res+=["tysięcy"]
                else:
                    res+=["tysiące"] 
            elif(s != 0) or (d != 0) or (j != 0):
                    res+=["tysięcy"]
        
        elif (i == 6):
            if  (d == 0) and (j == 1):
                res+=["milion"]
            elif(j >= 2) and (j <= 4):
                if(d == 1):
                    res+=["milionów"]
                else:
                    res+=["miliony"]
            else:
                res+=["milionów"]
        
        if (d == 1):
            if  (j == 0):
                res+=["dziesięć"]
            elif(j == 1):
                res+=["jedenaście"]
            elif(j == 2):
                res+=["dwanaście"]
            elif(j == 3):
                res+=["trzynaście"]
            elif(j == 4):
                res+=["czteraście"]
            elif(j == 5):
                res+=["piętnaście"]
            elif(j == 6):
                res+=["szesnaście"]
            elif(j == 7):
                res+=["siedemnaście"]
            elif(j == 8):
                res+=["osiemnaście"]
            elif(j == 9):
                res+=["dziewiętnaście"]
        else:
            if  (j == 1):
                res+=["jeden"]
            elif(j == 2):
                res+=["dwa"]
            elif(j == 3):
                res+=["trzy"]
            elif(j == 4):
                res+=["cztery"]
            elif(j == 5):
                res+=["pięć"]
            elif(j == 6):
                res+=["sześć"]
            elif(j == 7):
                res+=["siedem"]
            elif(j == 8):
                res+=["osiem"]
            elif(j == 9):
                res+=["dziewięć"]
            
            if  (d == 2):
                res+=["dwadzieścia"]
            elif(d == 3):
                res+=["trzydzieści"]
            elif(d == 4):
                res+=["czterdzieści"]
            elif(d == 5):
                res+=["pięćdziesiąt"]
            elif(d == 6):
                res+=["sześćdziesiąt"]
            elif(d == 7):
                res+=["siedemdziesiąt"]
            elif(d == 8):
                res+=["osiemdziesiąt"]
            elif(d == 9):
                res+=["dziewięćdziesiąt"]
            
        if (s == 1):
            res+=["sto"]
        elif(s == 2):
            res+=["dwieście"]
        elif(s == 3):
            res+=["trzysta"]
        elif(s == 4):
            res+=["czterysta"]
        elif(s == 5):
            res+=["pięćset"]
        elif(s == 6):
            res+=["sześćset"]
        elif(s == 7):
            res+=["siedemset"]
        elif(s == 8):
            res+=["osiemset"]
        elif(s == 9):
            res+=["dziewięćset"]
        
        i += 3

    revres = list(reversed(res))
    result = ""
    for e in revres:
        result += e + " "
    return result