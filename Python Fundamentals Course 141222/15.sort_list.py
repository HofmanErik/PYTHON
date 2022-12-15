#Exercise 2.7

def tel_klinkers(tekst):
    tekst = tekst.lower()
    tekst = tekst.split()
    list = []
    list2 = []
    for word in tekst:
        n = sum([word.count(v) for v in 'aeiouy'])
        list.append(n)
        list2.append(word)
    return list, list2

tekst = 'mies aap noot waternoodramp you'
var, words = tel_klinkers(tekst)

print(var, words)


