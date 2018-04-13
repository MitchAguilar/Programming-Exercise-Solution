a=(int)(input())
print("Lumberjacks:")
for i in range(a):
    bandera=True
    banderat=True
    b=input().split(' ')
    for e in range(len(b)):
        try:
            if (int)(b[(int)(e)]) < (int)(b[((int)(e))+1]):
                bandera=True
            else:
                bandera=False
                break
        except:
            pass
    for e in range(len(b)):
        try:
            if (int)(b[(int)(e)]) > (int)(b[((int)(e))+1]):
                banderat=True
            else:
                banderat=False
                break
        except:
            pass
    if((bandera==False and banderat==True)or(bandera==True and banderat==False)):
        print("Ordered")
    else:
        print("Unordered")
        
