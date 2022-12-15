#Exercise 1.9 (maak een getalraadspel).
from random import randint

secret = randint(1,100)
#print(secret)
guess = 0
counter = 0

while guess != secret:
    counter = counter + 1
    guess = int(input('Geef uw getal: '))
    if secret < guess:
        print('Lager...')
    elif secret > guess:
        print('Hoger...')
    elif guess == secret:
        print(f'Ja, {guess} is het juiste getal! In {counter} keer')
    else:
        pass
