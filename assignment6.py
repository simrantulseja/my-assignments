#ques-1)Create a function to calculate the area of a sphere by taking radius from user.
def calculate():
    x=int(input("enter the radius of sphere"))
    area=3.14*x*x
    print(area)

calculate()

#ques-2)Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
def perf(num):
    l=[]
    for i in range(1,num):
        if num%i==0:
            l.append(i)
        if sum(l)==num:
            return True

lower=1
upper=1000
for i in range(lower,upper+1):
   if( perf(i)):
       print("the number {} is a perfect number".format(i))

#ques-3)Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
x=int(input("enter the number"))
for i in range(1,11):
      m=x*i;
      print('{} * {} = {}'.format(x,i,m))

#ques-4)Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def pow(x, y):+

    if y == 1:
        return x

    if y != 1:
        return x * pow(x, y - 1)


a=int(input("enter first number"))
b=int(input("enter second number"))
print(pow(a,b))