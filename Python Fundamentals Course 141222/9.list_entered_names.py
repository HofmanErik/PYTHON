#Exercise 2.1 (maak een namenlijst doormiddle van een loop)
namen = []
yn = 'y'

while True:
    if yn == 'y':
        naam = input("Geef 'n naam op alstublieft: ")
        namen.append(naam)
    elif yn == 'n':
        break
    else:
        print('Geef een valide invoer alstublieft')
    yn = input('Wilt u een naam op geven? y/n')

namen.sort()
print('\nGesorteerde namen: ')
for naam in namen:
    print(naam)