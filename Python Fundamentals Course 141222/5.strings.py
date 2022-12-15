#Exercise 1.6 (experiment met strings).
t = input("Geef hier 'n willekeurige tekst: ")

print('\nIn upper (format): ',t.upper()+'.',
      '\nIn lower (format): ',t.lower()+'.',
      '\nIn capitalize (format): ',t.capitalize()+'.',
      '\nIn title format: ',t.title(),'.',
      '\nDit is slice van de eerste 3 letters: ',t[0:3],
      '\nHier zijn de spaties vervangen door "_": ',t.replace(' ', '_')+'\n')

if '?' in t[-1]:
    print('Je hebt de interpunctie "?" gebruikt in jouw zin.')
else:
    print(f'Geen "?" gebruikt in jouw tekst, de laatste letter was "{t[-1]}".')