x=0
while True:
    a=input().split(' ')
    if(a[0]==''):
        break
    y=(int)(a[0])
    b=(int)(1)
    c=(1)
    while (b<=y):
        c*=b
        b=b+1
    print(str(y)+'!')
    print(c)
print()
