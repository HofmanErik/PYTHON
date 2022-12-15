#Exercise 2.5 (creeer een functie die de tekst met astrix omhulst uitprint)

def banner(tekst=False):
    if tekst == True:
        tekst = input('Geef alstublieft uw tekst: ')
    else:
        pass
    banner = (len(tekst) + 6) * '*'+'\n'+f'*  {tekst}  *\n'+(len(tekst)+ 6) * '*'
    return banner

banner_var = banner('schoenenmaker')
print(banner_var)
