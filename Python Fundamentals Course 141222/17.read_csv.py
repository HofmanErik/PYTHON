#Exercise 2.9 (lees csv bestand en filter regels eruit).
import csv

file = 'ca-500.csv'

def open_csv(file):
    with open(file) as f:
        tekst = csv.DictReader(f, delimiter=';', quotechar='"')
        headers = f.readline().rstrip("\n").split(";")
        for line in f:
            columns = line.rstrip('\n').split(";")
            d = dict(zip(headers, columns))
            print(d)

open_csv(file)