a=(int)(input())
for i in range(a):
    c=(int)(input())
    for j in range(c):
        d=input().split(' ')
        ca=[]
        for h in d:
            ca[h]=(int)(d[h])
        ca.sort()
        print((ca[range(d)]-ca[0])*2)
