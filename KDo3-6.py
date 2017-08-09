import random
a=random.sample(range(10),3)
list_sorted_a = sorted(a)
z=len(list_sorted_a)
print (list_sorted_a)
b=random.sample(range(10),9)
list_sorted_b = sorted(b)
y=len(list_sorted_b)
print (list_sorted_b)
m=set(a)
n=set(b)
l=[]
c= m & n
print (" method 1 intersection to both sets",c)
c= m | n
print ("elemenst union to both sets",c)
c=m.issuperset(n)
print ("Is m superset of n",c)


i=0
j=0
for i in range(0,z):
  for j in range(0,y):
    if list_sorted_a[i]==list_sorted_b[j] :
       l.append(list_sorted_a[i])
    j=j+1
  i=i+1    
print("method 2",l)


