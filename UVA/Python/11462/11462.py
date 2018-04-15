while True:
  a=(str)(input())
  if str(a)=="0":
    break
  else:
    b=input().split(" ")
    c=list(map(int, b))
    c=sorted(c)
    d=list(map(str,c))
    print(" ".join(d))
