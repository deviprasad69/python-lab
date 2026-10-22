l=[]
print(l)
l.append(10)
l.append(20)
l.append(30)
l.append(40)
print(l)
l.pop()
print(l)
l.insert(1,10)
print(l)
l1=[60,70,80]
l.extend(l1)
print(l)
l.extend([100,80])
print(l)
l3=['prasad','10','maths','lion']
print(l3)
l3.extend([10,85])
print(l3)
l3.insert(3,'mango')
print(l3)
l3.append(90)
print(l3)
#mixed list
l4=['devi',10,'blue']
print(l4)
l4.append('10')
print(l4)
l4.insert(1,'chinmay')
print(l4)
l4.extend([50,'78'])
print(l4)
#slicing operations
a=[10,20,30,40,50,60,70,78,89]
print(a)
a1=a[::-1]
print(a1)
a2=a[3::]
print(a2)
a3=a[:3:]
print(a3)
a4=a[:8:2]
print(a4)
b=[10,'red',20,'green',30,'blue']
b1=b[::2]
b2=b[1::2]
print(b)
print(b1)
print(b2)
c=[10,20,'red','green',30,70,15.6,'blue']
n=len(c)
print(n)
c1=[]
c2=[]
for i in c:
    if isinstance(i,(int,float)):
        c1.append(i)
    else:
        c2.append(i)
print(c1)
print(c2)



