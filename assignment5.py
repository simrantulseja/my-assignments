#ques-1)
year = int(input("Please Enter the Year"))
 
if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)

#ques-2)
length=int(input("enter the length:"))
breadth=int(input("enter the breadth:"))
if(length==breadth):
     print("it is a square")
else:
     print("it is a rectangle")
     
#ques-3)
x=int(input("enter the age of first person"))
y=int(input("enter the age of second person"))
z=int(input("enter the age of third person"))
if(x>y):
    if(x>z):
      print("x is oldest")
    else:
      print("z is oldest")
else:
    if(y>z):
      print("y is oldest")
    else:
      print("z is oldest")

if(x<y):
    if(x<z):
      print("x is youngest")
    else:
      print("z is youngest")
else:
    if(y<z):
      print("y is youngest")
    else:
      print("z is youngest")

     
#ques-4)
age=int(input("enter the age:"))
gender=input("enter the gender")
ms=input("enter the marital status :")
if(gender == 'female'):
    print("she will work only in urban areas")
elif(gender=='male' and age>20 and age<40):
    print("he may work in anywhere")
elif(gender=='male' and age>40 and age<60):
    print("he may work in urban areas only")
else:
    print("ERROR")


#ques-5)
x=int(input("enter the quantity "))
cost=x*100
dis=10/100
if(cost>1000):
    cost=cost-dis
    print("cost is:" ,cost)
else:
    print("cost is:", cost)

#loops
#ques-1)
for i in range(10):
    x=int(input())
    print(x)
    
#ques-2)
x=True
while True:
    print("hello world")

#ques-3)
mylst=[]
x=int(input("enter the first element"))
y=int(input("enter the second element"))
z=int(input("enter the third element"))
w=int(input("enter the fourth element"))
u=int(input("enter the fifth element"))
mylst.append(x)
mylst.append(y)
mylst.append(z)
mylst.append(w)
mylst.append(u)
l=[]
for i in mylst:
   x=i*i
   l.append(x)

print(l)

#ques-4)
mylst=['simran',1,2.5,'smridhi',2,3.5,'subina',3,4.5]
a=[]
b=[]
c=[]
for i in mylst:
    if(type(i)==int):
       a.append(i)
    elif(type(i)==str):
       b.append(i)
    elif(type(i)==float):
       c.append(i)


print(a)
print(b)
print(c)


#ques-5)
num1=1
num2=100
for num in range(num1,num2+1):
    if num1>1:
       for i in range(2,num):
          if num%index==0:
             break
          else:
           print(num)
         
#ques-6)
for i in range(4):
   print('\n')
   for j in range(0,i+1):
     print('*' , end= ' ')

#ques-7)
mylst=[]
x=int(input("enter the first element"))
y=int(input("enter the second element"))
z=int(input("enter the third element"))
w=int(input("enter the fourth element"))
u=int(input("enter the fifth element"))
mylst.append(x)
mylst.append(y)
mylst.append(z)
mylst.append(w)
mylst.append(u)
num=int(input("enter the element to be searched"))
for i in mylst:
   if(i==num):
     mylst.remove(i)

print(mylst)

    
    

            


