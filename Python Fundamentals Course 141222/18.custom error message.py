#Exercise 2.10 (probeer een niet bestaand bestand te openen en geef een custom error bericht)
file = 'niet_bestaand.txt'

try:
    with open(file) as f:
        print(f)
except FileNotFoundError:
    print('Kan het bestand helaas niet vinden.')
except IOError as error:
    print('Kan het bestand helaas niet openen.')
except Exception as error:
    print(f'Iets anders aan de hand: ({error})')