# 6
def inch_to_cms(inch):
    return inch * 2.54

n=int(input("enter value in inches:"))
print(f" the corresponding value in cms is {inch_to_cms(n)}")


# 7
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n            

l=['aryan','ankit','abhishek']
print(rem(l, "an"))


# 8
def mul(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
mul(5)