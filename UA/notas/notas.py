a=(int)(input())
for i in range(a):
    b=(str)(input())
    d=0
    c=0
    e=0
    num=len(b)
    for j in range(num):
        try:
            if b[j]=='1' and b[j+1]=='0':
              c=c+10
              d=d+1
              e=e+1
            else:
              c2=int(b[j])
              c=c+c2
              d=d+1
        except IndexError:
            c2=int(b[j])
            c=c+c2
            d=d+1
    print("%.2f" % (c/(d-e)))

