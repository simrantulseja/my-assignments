my_list=[] #1st answer
\first=(input("enter first number"))
second=(input("enter second number"))
third=(input("enter third number"))
fourth=(input("enter fourth number"))
fifth=(input("enter fifth number"))

my_list.append(first)
my_list.append(second)
my_list.append(third)
my_list.append(fourth)
my_list.append(fifth)

print(my_list)
list1=["google","apple","facebook","microsoft","tesla"]#2nd answer
my_list.append(list1)
print(my_list)

hello=['p','r','o','g','r','a','m']#3rd answer
a=input("enter the number whose frequency is to be counted")
print(hello.count(a))

list2=[ 2,1,6,7,32,22]#fourth answer
list2.sort()
print(list2)

array1=[1,2,3,4,5]#5th answer
array2=[6,7,8,9,10]
array1.extend(array2)
print(array1)


lis=[]#6th answer
first=int(input("enter first number"))
second=int(input("enter second number"))
third=int(input("enter third number"))
fourth=int(input("enter fourth number"))
fifth=int(input("enter fifth number"))

lis.append(first)
lis.append(second)
lis.append(third)
lis.append(fourth)
lis.append(fifth)
countodd=0
counteven=0
for i in lis:
   if(i%2==0):
    counteven+=1
   else:
    countodd+=1
print("odd numbers=" ,countodd)
print("even numbers=", counteven)


#tupple questions
t=(1,2,3,4,5)#1st answer
print(t[::-1])


a=(22,34,65,89,90)#2nd answer
x=max(a)
y=min(a)
print("max element=" , x)
print("min element=", y)


#string questions
s="simran tulseja"#1st answer
print(s.upper())

s="102034597685"#2nd answer
print(str.isdigit())

a="hello world"#3rd answer
print(a.replace("world","simran"))
