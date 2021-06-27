def crossover(a, b):
    return a[0] < b[0] and a[1] > b[1]


def crossunder(a, b, i):
    return a[0] > b[0] and a[1] < b[1]
