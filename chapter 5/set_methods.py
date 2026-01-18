s={1,4,55,66,44,"dipika"}
print(s,type(s))


# set methods
s.add(566)
print(s,type(s))

print(len(s))
s.remove(4)
print(s)

print(s.clear())


# /union and intersection of set

s1={1,23,44,5}
s2={3,23,4,5}

print(s1.union(s2))
print(s1.intersection(s2))