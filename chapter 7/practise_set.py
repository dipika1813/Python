# n=int(input("enter a num:"))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")


# z=int(input("enter num:"))
# for i in range(1,11):
#     print(z*i)



# 2
# l=["harry","soham","sachin","rahul"]
# for name in l:
#     if(name.startswith("s")):
#         print(f"hello  {name}")



# 3
# n=int(input("enter the num:"))
# i=1
# while(i<11):
#     print(n*i,)
#     i+=1


# 4
n=int(input('enter a num:'))
for i in range(2,n):
    if(n%i==0):
        print("not a prime num")
        break
else:
    print("prime")


# 5
i=1
n=int(input("enter a num:"))
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)


# 6
n=int(input('enter num:'))
product=1
for i in range(1,n+1):
    product*=i

print(f"the factorial of {n} is {product}")
