# set unique unordered collection of element
# set is very fast than list

s = set()
se= {2,4,6,7,2}
print(type(s),type(se))

s.add(4)
s.add(0)
s.add(5)
s.add(7)
s.add(3)
s.add(4)
s.add(2)
print(s)
s.remove(0)
print(s)
print(4 in s)
print(s.union(se))
print(s.intersection(se))
print(s.difference(se))
