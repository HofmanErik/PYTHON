#Exercise 1.5 (dobbel 5 keer, geef de som van de dobbels).
from random import randint as dice

dice1 = dice(1,6)
dice2 = dice(1,6)
dice3 = dice(1,6)
dice4 = dice(1,6)
dice5 = dice(1,6)
sum = dice1 + dice2 + dice3 + dice4 + dice5

print(f'\ndice 1 = {dice1}',
      f'\ndice 2 = {dice2}',
      f'\ndice 3 = {dice3}',
      f'\ndice 4 = {dice4}',
      f'\ndice 5 = {dice5}',
      f'\nsum of dices is: {sum}')