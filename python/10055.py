try:
    while True:
        a=input().split(" ")
        b=int(a[0])
        c=int(a[1])
        print(abs(c-b))
except EOFError:
    pass
