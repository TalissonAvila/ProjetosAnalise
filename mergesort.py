# Código do MergeSort

def mergesort(array, pi, pf):
    if pi < pf:
        m = pi + (pf - pi) // 2
        mergesort(array, pi, m)
        mergesort(array, m + 1, pf)
        merge(array, pi, m, pf)


def merge(array, pi, m, pf):
    aux1 = m - pi + 1
    aux2 = pf - m
    left = [0] * aux1
    right = [0] * aux2
    for i in range(0, aux1):
        left[i] = array[pi + i]

    for j in range(0, aux2):
        right[j] = array[m + 1 + j]

    ml = 0
    mr = 0
    mo = pi

    while ml < aux1 and mr < aux2:
        if left[ml] <= right[mr]:
            array[mo] = left[ml]
            ml += 1
        else:
            array[mo] = right[mr]
            mr += 1
        mo += 1

    while ml < aux1:
        array[mo] = left[ml]
        ml += 1
        mo += 1

    while mr < aux2:
        array[mo] = right[mr]
        mr += 1
        mo += 1
