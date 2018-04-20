while True:
  a=(str)(input())
  if str(a)!="0":
    a = [int(x) for x in input().split()]
    a.sort()
    print(" ".join(map(str,a)))
  else:
    break
  
  
    #####soluton using bucle for read numbers
    #a = [int(x) for x in input().split()]
    #a.sort()
    #print(" ".join(map(str,a)))
    
    #####solution not using bucle
    #b=input().split(" ")
    #c=list(map(int, b))
    #c=sorted(c)
    #print(" ".join(map(str,c)))
