a=(int)(input())
while(a!=0):
    a-=1
    e=input().split(' ')
    b=(int)(e[0])
    c=(int)(e[1])
    if b<c:
        print("<")
    elif b>c:
        print(">")
    else:
        print("=")
