def generatorPhones(amount):
    arr = []
    for y in range(1, amount+1):
        number = ""
        for y in range(10):
            number += str(random.randint(0,9))
        arr.append(number if int(number) != 0 else "1111111111")
    return arr