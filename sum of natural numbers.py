n=int(input("enter a number"))
print(n)
sum=1
for i in range(1,n+1):
   if i>0:
       sum=sum*i
   elif i==0:
       print(1)
if n<0:
    print("not define")
print(sum)
 