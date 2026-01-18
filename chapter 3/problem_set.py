# 1 program to display user entered name followed by good afternoon using input()func

name=input('enter your name:')
print(f"good afternoon, {name}")


# 2 letter template with name and date

letter='''dear <|Name|>,
you are selected!
<|date|>'''
print(letter.replace("<|Name|>","dipika").replace("<|date|", "24 sepetember 2027"))


#3 program to detect double space in  a string
 
str="this  is   a   string "
print(str.find("a "))

#4 replace double sapce with single

new_str="my name  is   dipika  "
print(new_str.replace("  "," "))


#5 program to format following letter using escape seq char

l="dera harry,\n\t this python course is nice.\n thanks!"
print(l)