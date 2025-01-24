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
l1=['1','2','love','gupta','24']
print(''.join(l1))
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



l1=['lzzzzve','gupta','golu','myfue']
print(max(l1))
print(len(l1))
print(''.join(l1))
print(type(''.join(l1)))
x=(10,20,30,40)
(l1.extend(x))
print(l1)

l1.insert(0,("hello","myname"))
print(l1)

# print(l1.apppre("monu")) not supported by list but apppre is supported by array





