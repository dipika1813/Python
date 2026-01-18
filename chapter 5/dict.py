marks={"harry":55,"rajat":56,"mahesh":88}
print(type(marks))

print(marks["harry"])

print(marks.keys())

print(marks.items())
print(marks.values())

marks.update({"harry":99})
print(marks)


print(marks.get("harry1"))   #returns None
# print(marks['harry1'])     #returns an error
