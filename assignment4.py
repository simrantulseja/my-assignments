#ques-1) Reverse the whole list using list methods
#answer 1
lst=[ 1,2,3,4,5]
lst.reverse()
print(lst)

#ques-2) print all the uppercase letters from a string
#answer 2
x=input("enter a string")
for ch in x:
    if ch>='A' and ch<='Z':
       print(ch)


#ques-3)Split the user input on comma's and store the values in a list as integers.
#answer 3
x=input("enter a string")
a=x.split(",")
print(a)
b=[]
for i in a:
    b.append(int(i))

print(b)

#ques-4) check whether string is palindromic or not
#answer 4
x=input("Enter string:")
if(x==x[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")

#ques-5)make a deepcopy of a list and write the difference netween deep copy and shallow copy
#answer 5
import copy as c
lst_1=[1,2,[3,4],5]
lst_2=c.deepcopy(lst_1)
lst_1[2][0]='NOW'
lst_1[1]='HAHA'
print(lst_1)
print(lst_2)

lst_1=[1,2,[3,4],5]
lst_2=c.copy(lst_1)
lst_1[2][0]='NOW'
lst_1[1]='HAHA'
print(lst_1)
print(lst_2)


