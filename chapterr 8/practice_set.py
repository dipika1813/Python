# def greatest_no():
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c ):
#         return b
#     else:
#         return c

# a=int(input("enter a num:"))
# b=int(input('enter a num:'))
# c=int(input("enter a num:"))
# print(greatest_no())        



# # 2
# def f_to_c(f):
#     return 5*(f-32)/9

# f=int(input("enetr temperature in F:"))
# print(f_to_c(f))


# # 3
# print("a")
# print("b")
# print('c', end="")
# print("d", end="")


# 4
'''
sum(1)= 1
sum(2) = 1 + 2
sum(n) = sum(n-1) + n

'''
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n
# print(sum(4))


# 5
def pattern(n):
    if(n==0):
        return 
    print("*" * n)
    pattern(n-1)

pattern(3)