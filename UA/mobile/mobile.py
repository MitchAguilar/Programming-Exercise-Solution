data =[" ",".,?","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
val=(int)(input())
while val!=0:
  cas=(int)(input())
  va=input().split(' ')
  va2=input().split(' ')
  acum=""
  for i in range(cas):
    var=(int)(va[i])
    sret=data[var]
    var2=(int)(va2[i])
    thi=sret[var2-1]
    acum=acum+thi
    
  print(str(acum))
  
  val=val-1;
