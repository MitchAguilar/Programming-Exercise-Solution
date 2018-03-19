import math
try:
    while True:
        var=input().split(' ')
        a=(int)(var[0])
        b=(int)(var[1])
        h=(int)(var[2])
        if(a!=0 and b!=0 and h!=0):
            x=(int)(math.sqrt((h*h)+(b*b)))
            y=(int)(math.sqrt((a*a)+(h*h)))
            if((h==(int)(math.sqrt((a*a)+(b*b)))) or a==x or b==y ):
                print("right")
            else:
                print("wrong")
        else:
            break
except EOFError:
    pass
