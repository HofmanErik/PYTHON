#Exercise 1.8 (loop door de lijst)
tekst = input("Geef 'n willekeurige tekst: ")
counter = 0
letter_a = 0
letter_e = 0
letter_i = 0
letter_o = 0
letter_u = 0
letter_y = 0
aantal_vowels = 0
aantal_karakters = 0

while counter < len(tekst):
    for letter in tekst:
        if letter == 'a':
            letter_a = letter_a + 1
        elif letter == 'e':
            letter_e = letter_e + 1
        elif letter == 'i':
            letter_i = letter_i + 1
        elif letter == 'o':
            letter_o = letter_o + 1
        elif letter == 'u':
            letter_u = letter_u + 1
        elif letter == 'y':
            letter_y = letter_y + 1
        if ' ' in letter:
            pass
        else:
            aantal_karakters = aantal_karakters + 1
        counter = counter + 1

aantal_vowels = letter_a + letter_e + letter_i + letter_o + letter_u + letter_y

print(f'\nVond a {letter_a} keer.',
      f'\nVond e {letter_e} keer.',
      f'\nVond i {letter_i} keer.',
      f'\nVond o {letter_o} keer.',
      f'\nVond u {letter_u} keer.',
      f'\nVond y {letter_y} keer.',
      f'\nIn totaal {aantal_karakters} karakters.',
      f'\nDe tekst bevat {aantal_vowels} vowels.')

