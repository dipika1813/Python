# 1
a=int(input("enter a num:"))
b=int(input("enter a num:"))
c=int(input("enter a num:"))
d=int(input("enter a num:"))


if(a>b and a>c and a>d):
    print('a is greater')

elif(b>a and b>c and b>d):
    print("b is greater")

elif(c>a and c>b and c>d):
    print("c is greater")

else:
    print("d is greater")




# 2
math=int(input("enter marks:"))
bee=int(input("enter marks:"))
chem=int(input("enter marks:"))

total_percentage= (math + bee + chem )/3

if(total_percentage>=40 and math>=33 and bee>=33 and chem>=33):
    print("pass",total_percentage)

else:
    print("fail", total_percentage)


# 3

p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message=input("enter your comment:")

if((p1 in message)or (p2 in message)or (p3 in message)or (p4 in message)):
    print("this comment is a spam")

else:
    print("comment is not a spam")