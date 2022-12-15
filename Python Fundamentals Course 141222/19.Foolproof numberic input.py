#Exercise 2.11 (Create a function that asks to enter a number between two bounds given as arguments. The function should gracefully handle numbers outside of the bounds and also wrong types of input.)

def numeric_input(lower, upper):
    while True:
        try:
            user_input = int(input(f'Geef hier een getal tussen {lower} & {upper}: '))
        except Exception as error:
            print('Kan getal niet converteren, probeer opnieuw')
        if (user_input < lower) or (user_input > upper):
            raise Exception('Buiten de gevraagde range, probeer opnieuw')
            #print('Buiten de gevraagde range, probeer opnieuw!')
        else:
            print('Gefeliciteerd het is gelukt!')
            break
    return user_input

var = numeric_input(1, 20)