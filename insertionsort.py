def insertionsort(a):
    for i in range(1, len(a)):
        valor = a[i]
        j = i - 1
        while j >= 0 and a[j] > valor:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = valor
    return a
