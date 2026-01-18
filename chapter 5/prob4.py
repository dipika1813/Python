s=set()
s.add(20)
s.add(20.0) #20.0==20
s.add("20")

print(s)


s={}
name=input("enter name:")
lang=input("enter language name:")
s.update({name:lang})

name=input("enter name:")
lang=input("enter language name:")
s.update({name:lang})

name=input("enter name:")
lang=input("enter language name:")
s.update({name:lang})

name=input("enter name:")
lang=input("enter language name:")
s.update({name:lang})

print(s)