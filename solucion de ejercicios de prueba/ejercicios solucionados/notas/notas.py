a=(int)(input())
for i in range(a):
    b=(str)(input())
    d=0
    c=0
    e=0
    num=len(b)
    for j in range(num):
        if b[j]=='1' and b[j+1]=='0':
          c=c+10
          d=d+1
          e=e+1
        else:
          c=c+int(b[j])
          d=d+1
    #e=c/d
    print("%.2f" % (c/(d-e)))
