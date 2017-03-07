a=(int)(input())
while a!=0:
    a-=1;
    anc=0
    d="Y"
    z=5
    for e in range(z):
        ac=input().split(' ')
        if e!=0:
          x=(int)(ac[e])
          if ((x-anc)==1):
            d="Y"
          else:
            d="N"
            e=5
        anc=ac
    print(d)
