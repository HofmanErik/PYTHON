#Exercise 2.2
tekst = input('Plak uw tekst hier: ')
tekst = tekst.lower()
tekst = tekst.replace('.','').replace(',','')
tekst = tekst.split()
count = 0
unique = []
dict = {}

for word in tekst:
    if word not in unique:
        unique.append(word)
        dict[word] = 1
    else:
        dict[word] = dict[word] + 1

for key,value in dict.items():
    print(key, value)