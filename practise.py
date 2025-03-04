# x=10
# y=20
# print(x&y)

# # same memory address
# x=10
# y=10
# print(id(x))
# print(id(y))

# # immutable in nature
# #int
# x=10
# y=10
# print(id(x),id(y))

# # string 
# x="nearme"
# y="nearme"
# print(id(x),id(y))

# #tuple
# x=(10,20,"nearme")
# y=(10,20,"nearme")
# print(id(x),id(y))

# #list
# l1=[10,20,"nearme"]
# l2=[10,20,"nearme"]
# print(id(x),id(y))

#dict
# d1={"name":"rahul","age":30}
# d2={"name":"rahul","age":30}
# print(id(x),id(y))

# #set
# s1={10,20,"nearme"}
# s2={10,20,"nearme"}
# print(id(x),id(y))

# #frozenset
# fs1=frozenset({10,20,"nearme"})
# fs2=frozenset({10,20,"nearme"})
# print(id(x),id(y))


# str1=" i love  python"
# print(str1.find('p'))
# print(str1.find('z'))
# print(str1.split())
# print(str1.split("o"))
# print(str1.split("o",1))
# print(l1)


# list
# l1=['1','2','love','gupta','24']
# print(''.join(l1))
# print(str1.count('o'))


# x=[10]
# y=[10]

# print(id(y))
# y=[20]

# print(id(y))

# c=10
# d=10
# print(id(c),id(d))

# c=20
# print(id(c))



# l1=['lzzzzve','gupta','golu','myfue']
# print(max(l1))
# print(len(l1))
# print(''.join(l1))
# print(type(''.join(l1)))
# x=(10,20,30,40)
# (l1.extend(x))
# print(l1)

# l1.insert(0,("hello","myname"))
# print(l1)

# print(l1.apppre("monu")) not supported by list but apppre is supported by array

# l2=[10,20,30,40,50,15,5,25]
# l2.sort()
# print(l2)

# l2.reverse()
# print(l2)

# l2.sort(reverse=True)
# print(l2)

# print(l2.pop())
# l2.remove(15)
# print(l2)

# l2.clear()
# print(l2)

# del l2
# print(l2)

# l3=l2.copy()
# print(id(l2))
# print(l3)

# print(l2.index(30,-5))


# print(id(l2[0]))
# print(id(l2[1]))
# print(id(l2[2]))
# print(id(l2[3]))
# print(id(l2[4]))
# print(id(l2[5]))


# import sys

# x="lovekushgupta"
# l4=[15,15]
# t1=(45,45)
# y=21542
# print(sys.getsizeof(x))
# print(sys.getsizeof(l4))
# print(sys.getsizeof(t1))
# print(sys.getsizeof(y))

# print(len(l2))
# print(l2)


# s1={'1','2','love','gupta','24'}
# print(s1)
# print(type(s1))
# print(id(s1{-1}))

# print(max(s1))
# s1.clear()
# print(s1)
# s1.add(50)
# print(s1)

# s1.add(50)
# print(s1)

# t5=(50,1,2,3,4)
# l5=[50,1,2,3,4]
# s1.add(t5)
# print(s1)

# s1.update(l5)
# print(s1)

# s2={3,6,7,8}
# s3={3,6,1,2,4,5}

# print(s2.union(s3))
# print(s2.intersection(s3))
# s3.intersection_update(s2)
# print(s3)

# print(s2.difference(s3))
# s3.difference_update(s2)
# print(s3)

# print(s2.symmetric_difference(s3))

# s2.

# s="neeraj"
# l=[1,2,3,4]
# s9={'neeeraj','rahul','jai'}
# print(frozenset(s9))
# print(type(frozenset(s9)))
# print(frozenset(l))
# print(type(frozenset(s9)))


x=20
y=10
z=30
# if(x>y):
#     if(x>z):
#         print(f'{x} is greater')
#     else:
#         print(f'{z} is greater')
# else:
#     if(y>z):
#         print(f'{y} is greater')
#     else:
#         print(f'{z} is greater')


# if(x>y and x>z):
#     print("x is greater")

# else:
#     if (y>z):
#          print("y is greater")
#     else:
#          print("z is greater")


# if(x>y and x>z):
#     print("x is greater")
# elif(y>z):
#     print("y is greater")
# elif(z>y):
#      print("z is greater")

# n=input("enter any value")
# x=len(n)
# x=(n.__len__())
# print(x)
# print(type(n))
# n=int(n)
# print(type(n))
# revers=0
# while n>0:
#       x=x-1
#       revers=revers+((n%10)*(10**(x)))
#       n=n//10
    
# print(revers)  

# char to ascii with ord()
# ascii to char with chr()  
# range function is used --range(start,stop, step)
# j=range(11,0,-1)
# print(j)
# print(list(j))
# for i in n:
#       print(i)

# nam=input("enter any value")
# g=len(nam)-1
# renam=""
# while g>=0:
#       renam+=nam[g]
#       g=g-1
# print(renam)    
#   


# print(x)
# print(type(x))

# n=5
# i=0
# while i<n:
#     print(' '*(i)+' *'*(n-i))
#     i=i+1
# while i<n:
#     print(' '*(n-i)+' *'*(i))
#     i=i+1

# lcm 
# x=int(input("enter first number"))
# y=int(input("enter second number"))
# z=maxno=max(x,y)
# while True :
#       if maxno%x==0 and maxno%y==0 :
#           print(maxno)
#           break
#       maxno=maxno+z   


# hcf
# minno=min(x,y)
# i=1
# while i<=minno :
#       if x%i==0 and y%i==0 :
#           hcf=i
#       i=i+1
# print(hcf) 

#palindrom
# x=eval(input("enter your value"))
# g=len(x)-1 #lastindex
# count=-1 
# i=0
# while i<=g//2:
#       if(x[i]!=x[g-i]):      #if(x[i]!=x[-1-i])
#         break
#       else:  
#         count=count+1
#       i=i+1

# if(count==(g//2)):
#     print("palindrom")
# else:
#     print("not palindrom")     

# ------------------------using range-------------------------------

# for i in range(g,g//2,-1):
#     if(x[i]!=x[g-i]): 
#         print(x[i],x[g-i])    
#         break
#     else:  
#         count=count+1
      
# if(count==(g//2)):
#     print("palindrom")
# else:
#     print("not palindrom")  
              
    
#function
# def function_name(parameters):
#     "doc string optional"
#     function body
#     return

# def add(x,y):
#     "addition function"
#     print(x,y)
#     print(x+y)
#     return

# add(4,5)    
# add(y=4,x=5)
# print(add.__doc__)
# print(dir(add))#internal function details dekhne ke liye internal method use karte hai


# def add(*n):
#    print(n)
#    print(type(n))
#    sum=0
#    for i in n:
#     sum+=i
#    return sum 


# x=eval(input("enter your value"))
# print(add(*x))

# def show(**n):
#    print(n)
#    print(type(n))
#    for key,value in n.items():   #n.keys()//n.values()
#       print(f'my{key}is{value}')

# show(name="lovekush", age=21)  

# n=x=int(input("enter your number"))
# sum=0
# while n>0:
#    sum+=n%10
#    n=n//10

# if(x%sum==0) :
#    print("harsad number") 
# else:
#    print("not harsad no.")


#anagrams
# string1=input("enter your first string ")
# string2=input("enter your 2nd string ")

# if(sorted(string1)==sorted(string2)):
#    print("anagrams")
# else:
#    print("not anagrams")   

# n=x=int(input("enter your number"))
# n=n**2
# sum=0
# while n>0:
#    sum+=n%10
#    n=n//10

# if(sum==x) :
#    print("neon") 
# else:
#    print("not neon no.")



# n=x=int(input("enter your number"))
# def factorial(n):
#    fact=1
#    while(n>0):
#       fact=fact*n
#       n=n-1
#    return fact

# sum=0
# while n>0:
#    last_digit=n%10
#    sum+=factorial(last_digit)
#    n=n//10

# if(sum==x) :
#    print("peter") 
# else:
#    print("not peter no.")

# n=r=5
# i=1
# while n>0:
#    print(" "*(r-i)," *"*i)
#    i=i+1
#    n=n-1

# string=input("enter -")
# capital=0
# small=0
# num=0
# for x in string:
#    if x>=chr(65) and x<=chr(90):  #ifx>=A and x<=Z:
#       capital=capital+1
#    elif  x>=chr(97) and x<=chr(122): #elif x>=a and x<=z:
#       small=small+1
#    elif  int(x)>=0 and int(x)<=9:   
#       num=num+1
# print("capital_letter-",capital,"small_letter-",small,"number-",num)      


##vowels and consonents
# string2=input("enter any string-")
# vowel="aeiouAEIOU"
# countvow=0
# countconso=0
# for x in string2:
#    if x in vowel: #if x=="a"or"e"or"i"or"o"or"u"or"A"or"E"or"I"or"O"or"U": 
#       countvow=countvow+1
#    else:
#       countconso=countconso+1   
# print("vowels-",countvow,"consonents-",countconso)



#map() function higher order function
# syntax- map(functionname,collection)


# def squar(x):
#    if x%2==0:
#      return x+1
#    else:
#       return x+2  

# l1=eval(input("enter any numeric collection:-"))

# res=map(squar,l1)
# print(res)
# print(list(res))

# u=4,
# print(type(u))

# def add(x,y,z):
#     return x+y+z

# l1=eval(input("enter any numeric collection:-"))
# l2=eval(input("enter any numeric collection:-"))
# l3=eval(input("enter any numeric collection:-"))

# res=map(add,l1,l2,l3)
# print(res)
# print(list(res))


# def outer_fun(fun1):
#   def inner_fun():
#     print("before")
#     fun1()
#     print("after")
#   return inner_fun

# @outer_fun
# def fun():
#   print("this is function")

# res=outer_fun(fun)    
# print(res)
# res()  
# fun()


# def outer_f(funct):
#   def inner_f(x,y,z):
#     x=x+5
#     y=y+5
#     z=z+5
#     print(funct(x,y,z))
#   return inner_f  

# @outer_f
# def funt(x,y,z):
#   return x+y+z

# res=outer_f(funt)
# res(10,20,30)
# funt(x,y,z)


#modules- is a file that contains function and variable and class and methods and python code 
# collection of modules is called package, this folder must contain __init__.py file in it
# A single Python file containing code is considered a "module," while a directory that holds multiple related modules together is called a "package". 
# Key points about packages:
# Organization:
# Packages allow you to organize related modules into a hierarchical structure within a directory. 
# __init__.py file:
# A special file named __init__.py is usually present within a package directory to signify it as a package. 

# x=10
# y=20
# z=30

# def add(x,y,z):
#     print(x+y+z)


# class student:
#     ''' student details'''  
#     name='lovekush'
#     quali='BE'
    # self.address="nehru nagar"

    # def __init__(self,name,age,marks):
    #     print("i am parameterized constructor")
      
    #     self.age=age
    #     self.marks=marks
     

    
    # def new_fea(self,city):  # self is a reference variable is used to point  object of current class # work similar like this pointer in cpp
    #     self.p=city
    #     print("i am constructor") 
    # def show(self):
    #     print(self.name,self.age, self.marks,self.p,self.schoolnam)     


# print (dir(student)) #------> given all magic method    
# print(student.__doc__)  # print class comment

# print(student)
#vari=student #here only class load to another variable
# print(vari)
#obj=student("raj",23)  #class name with parenthesis  is used to make obj of class parenthesis is used to invoke constructor of class ,constructior is used to initialise object of class

# obj=student("lovekush",23,98)  #class name with parenthesis  is used to make obj of class parenthesis is used to invoke constructor of class ,constructior is used to initialise object of class
# # print(obj)
# obj.schoolnam="shss"
# obj.new_fea("bhopal")
# obj.show()
# print(obj.schoolnam)
# print(obj.name)



#static variable and static class

# class Student :
#     school="shss"  #declaration of static  variable
#     count=0
#     def __init__(self):
#         Student.count=Student.count+1

#     def new(self):
#         Student.city="bhopal"   
#     def show():
#         print(Student.city,Student.count)

# obj1=Student()
# obj1.new()
# print(Student.count)
# Student.show()
       

class book:
    price=100
    totalpages=500
    def _init_(self,title,author):
        self.title=title
        self.author=author
    @classmethod    
    def update(cls,nprice,npage):
        cls.price=nprice
        cls.totalpages=npage

    @classmethod    
    def addNew(cls,author):
        cls.author2=author
    def show(self):
        print(self.author,self.title,book.price,book.totalpages)
    @staticmethod
    def welcome():
        print("welcome to my web pages")
    @staticmethod
    def thanx():
        print("thanks for visit")    

publisher1=book("python","harsh")
publisher1.show()
publisher1.update(2000,500)       
publisher1.show()

print(publisher1.price)
