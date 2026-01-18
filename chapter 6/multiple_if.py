a=int(input("enter an age:"))

# if statement no 1
if(a%2==0):
    print("even")
# end of if statement no 1
    
# if statement no 2
if(a>=18):
    print("you are eligible")

elif(a<0):
    print('you entered an invalid age')

else:
    print("you are not eligible")

# end of if statement no 2

print("good bye")