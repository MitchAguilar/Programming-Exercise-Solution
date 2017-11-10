while True:
    a=input()
    if a=='0':
        break
    b=0
    c=0
    for i in range(len(a)):
        res=(int)(a[i])
        if i%2==0:
            b=b+res
        else:
            c=c+res
    res=b-c
    if res%11==0:
        print(str(a)+" is a multiple of 11.")
    elif res==0:
        print(str(a)+" is a multiple of 11.")
    else:
        print(str(a)+" is not a multiple of 11.")
