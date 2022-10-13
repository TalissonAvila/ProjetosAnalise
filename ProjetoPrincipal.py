import random
from InsertionSort import insertionSort
from mergeSort import mergeSort
import time

n = []
tamanho_random = random.randint(10, 21)
vetor_auxiliar = []
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
vetor5 = []
vetor6 = []
vetor7 = []
vetor8 = []
vetor9 = []
vetor10 = []

for i in range(10):
    n.append(random.randint(10, 10001))

for i in range(n[0]):
    vetor1.append(random.randint(n[0]*-2, n[0]*2 + 1))

for i in range(n[1]):
    vetor2.append(random.randint(n[1]*-2, n[1]*2 + 1))

for i in range(n[2]):
    vetor3.append(random.randint(n[2]*-2, n[2]*2 + 1))

for i in range(n[3]):
    vetor4.append(random.randint(n[3]*-2, n[3]*2 + 1))

for i in range(n[4]):
    vetor5.append(random.randint(n[4]*-2, n[4]*2 + 1))

for i in range(n[5]):
    vetor6.append(random.randint(n[5]*-2, n[5]*2 + 1))

for i in range(n[6]):
    vetor7.append(random.randint(n[6]*-2, n[6]*2 + 1))

for i in range(n[7]):
    vetor8.append(random.randint(n[7]*-2, n[7]*2 + 1))

for i in range(n[8]):
    vetor9.append(random.randint(n[8]*-2, n[8]*2 + 1))

for i in range(n[9]):
    vetor10.append(random.randint(n[9]*-2, n[9]*2 + 1))


def tempo(vetor):
    a = []
    b = []
    soma = 0
    somab = 0
    for i in range(tamanho_random):
        inicial = time.time()
        insertionSort(vetor)
        final = time.time()
        a.append(final-inicial)

        inicial = time.time()
        mergeSort(vetor, 0, len(vetor) -1)
        final = time.time()
        b.append(final - inicial)

    for i in range(len(a)):
        soma += a[i]
        somab += b[i]

        media = soma / tamanho_random
        mediab = somab / tamanho_random

    print(f'Tamanho do vetor: {len(vetor)}\n'
    f'Media Insertion Sort: {media}')
    print('-'*30)
    print(f'Tamanho do vetor: {len(vetor)}\n'
    f'Media Merge Sort: {mediab}')

tempo(vetor1)
print('-'*30)
tempo(vetor2)

