# # permanent data storage 
# # type of file- text file-----source code file data(.py exten)
# # 2nd binary file --- store byte code file that is convert from source code file (.pyc exten)
# 3rd one is csv file ----here data store in key value form


# f=open('n1.txt','w')
# print(f.name)
# print(f.mode)
# print(f.writable())
# f.write("gupta\nkush\nhello")

# f.write("my name is lovekush")
# content=f.read()
# print(content)
# print(f.closed)
# print(f.readable())


# f.read(n) # no of character
# f.readline() #single line read
# f.readlines() # multifle line
# f.tell()  #cursor position
# f.seek(where we move,move from (0,1,2)) # for cursor movement 0-> for starting point , 1-> for current point, 2->from last position (negative index from last)


# f=open('n4.txt','w+')

# print(f.readable())
# print(f.writable())
# print(f.closed)

#binary file
# source code ko byte code me change karne ke liye pickling use karte hai, pickle ak module hai, dump is used to convert in json (byte bytearray and string )
import pickle
# f=open('first.dat','ab')
# data=[10,20,30,'lovekush']
# pickle.dump(data,f)
# f.close()

# f=open('first.dat','rb')
# data=pickle.load(f)
# print(data)

fi=open('second.dat','rb')
print(fi.tell())  #for print cursor posittion in file
# fi.write("hello iam lovekush gupta i am form jabalpur and recently reside at bhopal")
# print(fi.tell()) 

data=fi.read()
print(data)
print(fi.tell())
data1=fi.read()
print(data1)

fi.seek(-10,2)
fi.seek(-20,1)
fi.seek(-5,1)
print(fi.tell()) 
print(fi.read())

# 7types of operator , in python and 3 isgiven value and 4 are gives boolen value