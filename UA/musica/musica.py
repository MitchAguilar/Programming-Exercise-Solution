a=input().split(' ')
if a[0] > a[1] and a[1] > a[2] and a[2] > a[3] and a[3] > a[4] and a[4] > a[5] and a[5]>a[6] and a[6] > a[7]:
    print("descending")
elif a[0] < a[1] and a[1] < a[2] and a[2] < a[3] and a[3] < a[4] and a[4] < a[5] and a[5]< a[6]  and a[6] < a[7]:
    print("ascending")
else :
    print("mixed")
