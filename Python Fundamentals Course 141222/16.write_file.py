#Exercise 2.8 (tekst schrijven naar bestand).
file = 'demo.txt'

def write():
    print('Function: write')
    with open(file, 'w') as f:
        for i in range(10):
            print(f'Wrote : Line{i}')
            f.write(f'Line{i}\n')

def read():
    print('Function: read')
    with open(file) as f:
        for line in f:
            print(line.rstrip())

write()
read()


