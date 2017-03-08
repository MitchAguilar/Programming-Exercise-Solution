x=0
while True:
    a=input().split('\n')
    y=(int)(a[0])
    if None==a[0]:
        break
    b=(int)(1)
    c=(1)
    while (b<=y):
        c*=b
        b=b+1
    print(str(y)+'!')
    print(c)
print()
