try:
    while True:
        a=input().split(" ")
        b=(int)(a[0])
        c=(int)(a[1])
        print(str(b^c))
except EOFError:
    pass
