try:
    while True:
        a=input().split(' ')
        b=(int)(a[0])
        c=(int)(a[1])
        n=b
        leng=0        
        while n!=1:
            leng=leng+1
            if (n%2!=0):
                n=(3*n)+1
            else:
                n=n/2
        n=c
        while n!=1:
            leng=leng+1
            if(n%2!=0):
                n=(3*n)+1
            else:
                n=n/2
        print(str(b)+" "+str(c)+" "+str(leng+1))
except EOFError:
    pass

