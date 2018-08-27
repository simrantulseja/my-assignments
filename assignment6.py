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

#ques-1)
dict1={}
for i in range(1,5):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dict1[key] = value
print(dict1)0


#question2
dict1={}
dict2={}
for i in range(1,3):
    dict2={}
    name = input("Enter name ")
    for j in range(1,3):
              sub=input("enter subject")
              marks=int(input("enter marks"))
              dict2[sub]=marks
    dict1[name]=dict2
print(dict1)
student=input("enter the student's name whose marks u want to see")
print(dict1[student])
    

#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

class circle:
    def __init__(self,r):
        self.radius=r
    def getarea(self):
        return self.radius**2*3.14
    def getcircumference(self):
        return 2*3.14*self.radius

r=int(input("enter radius of circle"))
ob=circle(r)
print("AREA: ",ob.getarea())
print("CIRCUMFERENCE: ",ob.getcircumference())


#Q.2- Create a Student class and initialize it with name and roll number. Make methods to : 
#     1. Display - It should display all informations of the student. 
#     2. setAge - It should assign age to student 3. setMarks - It should assign marks to the student.

class student:
    def __init__(self,n,r):
        self.name=n
        self.rollno=r
    def display(self):
        print ("Name:",self.name)
        print ("Roll no:",self.rollno)
        print ("Age:",self.age)
        print ("Marks:",self.marks)
    def setAge(self,age):
        self.age=age
    def setMarks(self,marks):
        self.marks = marks
s1=student('Priya',650)
s1.setAge(20)
s1.setMarks(98)
s1.display()


#Q.3- Create a Temperature class and create two methods: 
#     1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
#     2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class Temperature():
  def  convertFahrenhiet(self,celsius):
    return (celsius*(9/5))+32
  def convertCelsius(self,farenhiet):
    return (farenhiet-32)*(5/9)

ob=Temperature()
temp=int(input("enter temperature in celcius"))
print ("Temperature in Fahrenhiet:",ob.convertFahrenhiet(temp))
temp=int(input("enter temperature in Fahrenhiet"))
print ("Temperature in Celcius:",ob.convertCelsius(temp))


#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings .Make methods to- 
#     1. Display-Display the details. 
#     2. Add- Add the movie details.

class MovieDetails:
    def __init__(self,name,year,rating):
        self.Artistname=name
        self.ReleaseYear=year
        self.ratings=rating
    def display(self):
        print("Movie Name:",self.moviename)
        print("Artist Name:",self.Artistname)
        print("Year of Release:",self.ReleaseYear)
        print("Ratings of Movie:",self.ratings)
    def add(self,mname):
        self.moviename=mname
ob=MovieDetails("Rajkumar Rao",2017,9)
ob.add("Newton")
ob.display()
        

#Q.5- Create a class Animal as a base class and define method animal_attribute.
#     Create another class Tiger which is inheriting Animal and access the base class method.

class animal:
    def animal_attribute(self,sound,habitat):
        self.sound=sound
        self.habitat=habitat

class tiger(animal):
    def info(self):
        animal.animal_attribute(self,"Roar","Forest")
        self.kind="Tiger"
    def display(self):
        print ("Hello i am {}.I live in {} and I {}.".format(self.kind,self.habitat,self.sound))

ob=tiger()
ob.info()
ob.display()


#Q.6- What will be the output of following code?

'''ANSWER:- Output will be:
            "A B"
            "A B" 
'''

#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area.
#      Create class rectangle and square which inherits shape and access the method Area.

class shape:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
class rectangle(shape):
    def __init__(self):
        l=int(input("enter length of rectangle"))
        b=int(input("enter breadth of rectangle"))   
        shape.__init__(self,l,b)
    def area(self):
        print("Area of Rectangle is:",shape.area(self))
class square(shape):
    def __init__(self):
        side=int(input("enter side of square"))
        shape.__init__(self,side,side)
    def area(self):
        print("Area of Square is:",shape.area(self))

rect=rectangle()
rect.area()
sq=square()
sq.area()
