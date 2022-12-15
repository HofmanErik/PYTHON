#Exercise 1.7 (print stage of life based on age).
age = int(input('Please give your age: '))

if age >= 0 and age <= 2:
    print('Baby')
elif (age > 2) and (age <= 4):
    print('Toddler')
elif (age > 4) and (age <= 13):
    print('Kid')
elif (age > 13) and (age <= 20):
    print('Teenager')
elif (age > 20) and (age <= 65):
    print('Adult')
elif age < 0 or age > 140:
    print('Something else...')
else:
    print('Elder')