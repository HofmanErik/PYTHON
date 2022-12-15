#Theorie
import math as m
import random
import random as r

getal1 = 10
getal2 = 6.1
getal3 = -1
getal4 = complex(5) #-5 wortel i
bool = True

print(type(getal1))
print(type(getal2))
print(type(getal3))
print(type(getal4))
print(m.ceil(getal2))
print(type(bool))

print(hex(id("blablabla")))
print(bin(id("blablabla")))
#woorden zijn inmutable, ook al replace je ze, de data blijft hetzelfde,
#Je krijg nieuwe string terug
print('blablabla'.replace('a', ' - '))
print(len('blablabla hoi')/2)

getallenlist = list(range(100, 200))
getallenlist.remove(101)
getallenlist.reverse()
find100 = getallenlist.index(100)
print(getallenlist)
print(find100)

getallenlist.append("product")
print(getallenlist)

getallenlist.extend([1,2,3,4,5])
print(getallenlist)

