while True:
    a=input().split(' ')
    if a[0]!='0':
        print("".join(reversed([("".join(reversed(a[1])))[i:i+((int)(len((str)(a[1]))/(int)(a[0])))] for i in range(0,len((str)(a[1])),((int)(len((str)(a[1]))/(int)(a[0]))))])))
    else:
        break
