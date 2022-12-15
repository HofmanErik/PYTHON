#Exercise 2.3 (genereer een wachtwoord minimaal 6 karakters)
import random

capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercases = 'abcdefhijklmnopqrstuvwxyz'
numbers = '0123456789'
specials = '!@#$%^&*()_+'
part1 = random.choices(capitals, k=3)
part2 = random.choices(lowercases, k=3)
part3 = random.choices(numbers, k=3)
part4 = random.choices(specials, k=3)
characters = part1, part2, part3, part4

characters = random.shuffle(characters)
password = "".join(characters)
print(characters)


