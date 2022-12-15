#Exercise 1.3 (jaar moet deelbaar zijn door 4 en 400 maar niet door 100).
jaar = int(input('Geef een jaartal alstublieft: '))
if (jaar % 100 == 0) and (jaar % 400 == 0):
    print(f'{jaar} is WEL een schrikkeljaar')
elif (jaar % 100 != 0) and (jaar % 4 == 0):
    print(f'{jaar} is WEL een schrikkeljaar')
else:
    print(f'{jaar} is GEEN schrikkeljaar')