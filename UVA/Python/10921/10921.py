try:
    while True:
        a=(str)(input())
        b=""
        for i in range(len(a)):
            if a[i]=="A":
                b=b+"2"
            elif a[i]=="B":
                b=b+"2"
            elif a[i]=="C":
                b=b+"2"
            elif a[i]=="D":
                b=b+"3"
            elif a[i]=="E":
                b=b+"3"
            elif a[i]=="F":
                b=b+"3"
            elif a[i]=="G":
                b=b+"4"
            elif a[i]=="H":
                b=b+"4"
            elif a[i]=="I":
                b=b+"4"
            elif a[i]=="J":
                b=b+"5"
            elif a[i]=="K":
                b=b+"5"
            elif a[i]=="L":
                b=b+"5"
            elif a[i]=="M":
                b=b+"6"
            elif a[i]=="N":
                b=b+"6"
            elif a[i]=="O":
                b=b+"6"
            elif a[i]=="P":
                b=b+"7"
            elif a[i]=="Q":
                b=b+"7"
            elif a[i]=="R":
                b=b+"7"
            elif a[i]=="S":
                b=b+"7"
            elif a[i]=="T":
                b=b+"8"
            elif a[i]=="U":
                b=b+"8"
            elif a[i]=="V":
                b=b+"8"
            elif a[i]=="W":
                b=b+"9"
            elif a[i]=="X":
                b=b+"9"
            elif a[i]=="Y":
                b=b+"9"
            elif a[i]=="Z":
                b=b+"9"
            else:
                b=b+a[i]
        print(b)
except EOFError:
    pass
