#Write a script that remove duplicates from a list
a = ["1", 1, "1", 2]
a = list(set(a))
print(a)

#If you want to keep the order, you need OrderedDict
from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)


#Alternate

a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)

print(b)

