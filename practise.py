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
x=eval(input("enter your value"))
g=len(x)-1 #lastindex
count=-1 
i=0
while i<=g//2:
      if(x[i]!=x[g-i]):      #if(x[i]!=x[-1-i])
        break
      else:  
        count=count+1
      i=i+1

if(count==(g//2)):
    print("palindrom")
else:
    print("not palindrom")     
              
    
