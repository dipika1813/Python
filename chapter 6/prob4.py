username=input("enter username:")

if(len(username)<10):
    print("contains less than 10 char")

else:
    print("contains more than 10 char")



# 5
l=["harry",'shubham',"divya"]

name=input("enter your name:")

if(name in l):
    print("your name is in list")

else:
    print("your name is not in list")



# 6
marks=int(input("enter your marks:"))

if(marks<=100 and marks>=90):
    grade="Ex "
elif(marks<=90 and marks>=80):
    grade="A "
elif(marks<=80 and marks>=70):
    grade="B "
elif(marks<=70 and marks>=60):
    grade="C "
elif(marks<=60 and marks>=50):
    grade="D "
elif(marks<=50 and marks>=40):
    grade=" F"

print("your grade is",grade)


# 7

post=input("enter your post:")

if("dipika" in post):
    print("this post is talking about dipika")

else:
    print("this post is not talking about dipika")