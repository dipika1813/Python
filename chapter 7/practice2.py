# 7
# (for n=3)

n=int(input("enter a num:"))
for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"* (2*i-1),end="" )
    print("\n")
    


# 8
n=int(input("enter a num:"))
for i in range(1,n+1):
    
    print("*"* i,end="" )
    print("")


# 9
n=int(input("enter a num:"))
for i in range(1,n+1):
    if(i==1 or i==n):  
        print("*"* n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")


# 10 #reverse table 
n=int(input("enter a num:"))
for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")