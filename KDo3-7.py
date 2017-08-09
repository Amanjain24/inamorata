a=input("number please")
a=int(a)
if a==2:
  print ("prime")
else:
 c = [x for x in range(2, a) if a % x == 0]
 if len(c)>0:
   print("NOT PRIME method 1")
 else : print ("prime11")

b=2
while (b!=a):
  if a%b==0 & a!=b:
    print("not a prime")
    break 
  else:
    b=b+1 

if(b==a):
 print("prime")  