try:
    while True:
        a=input().split(' ')
        i=(int)(a[0])
        j=(int)(a[1])
        #tem
        temi=i
        temj=j
        if (i > j):
            i,j=j,i
        max_cycle_length = 0
        cycle_length=0
        while i <= j :
            n = i
            cycle_length = 1
            while n != 1 :
                if n % 2 == 1 :
                    n = 3 * n + 1
                else:
                    n /= 2
                cycle_length=cycle_length+1
            if cycle_length > max_cycle_length:
                max_cycle_length = cycle_length
            i=i+1
        print(str(temi)+" "+str(temj)+" "+str(max_cycle_length))
except EOFError:
    pass

