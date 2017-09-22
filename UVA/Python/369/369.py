import math
while True:
    a=input().split(" ")
    if a[0]=="0" and a[1]=="0":
        break
    print(a[0]+" things taken " +a[1]+" at a time is "+str(round((math.factorial((int)(a[0])))/(math.factorial((int)(a[0])-(int)(a[1]))*math.factorial((int)(a[1])))))+" exactly.")
