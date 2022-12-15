#Exercise 2.6

def frange(start, stop, step=1, endpoint=False):
    numbers = []
    number = 0

    while True:
        number = number + 1
        if endpoint:
            numbers.append(number)
            if number > stop:
                break
        else:
            numbers.append(number)
            if number == stop:
                break
    return numbers

rangeVar = frange(1, 100, endpoint=True)
print(rangeVar)


