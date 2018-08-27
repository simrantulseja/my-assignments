#answer-1)
try:
    a=3
    if a<4:
          a=a/(a-3)
          print(a)

except ZeroDivisionError:
    print("you can't divide by zero")


#answer-2)
try:
   l=[1,2,3]
   print(l[3])
except IndexError:
    print("index out of range")

#answer-3)
An exception
NameError: hi there

#answer 4)
-5.0
a/b result in 0

#answer-5)
1.import error

try:
     from _foo import *
except ImportError:
     print("wrong import")

2.value error

try:
     x=int(input("enter a number"))
    
except ValueError:
    print("only integer value allowed")

3.index error
try:
    l=[1,2,3]
    print(l[3])
except IndexError
    print("index out of range")




  
