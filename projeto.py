import random
from insertionsort import insertionsort
from mergesort import mergesort
import time
import pandas as pd
import matplotlib.pyplot as plt


n = []
tamanho_random = random.randint(10, 21)
vetor = []

for i in range(10):
    vetor_aux = []
    vetor.append(vetor_aux)
    n.append(random.randint(10, 10001))

for i in range(n[0]):
    vetor[0].append(random.uniform(n[0]*-2, n[0]*2 + 1))

for i in range(n[1]):
    vetor[1].append(random.uniform(n[1]*-2, n[1]*2 + 1))

for i in range(n[2]):
    vetor[2].append(random.uniform(n[2]*-2, n[2]*2 + 1))

for i in range(n[3]):
    vetor[3].append(random.uniform(n[3]*-2, n[3]*2 + 1))

for i in range(n[4]):
    vetor[4].append(random.uniform(n[4]*-2, n[4]*2 + 1))

for i in range(n[5]):
    vetor[5].append(random.uniform(n[5]*-2, n[5]*2 + 1))

for i in range(n[6]):
    vetor[6].append(random.uniform(n[6]*-2, n[6]*2 + 1))

for i in range(n[7]):
    vetor[7].append(random.uniform(n[7]*-2, n[7]*2 + 1))

for i in range(n[8]):
    vetor[8].append(random.uniform(n[8]*-2, n[8]*2 + 1))

for i in range(n[9]):
    vetor[9].append(random.uniform(n[9]*-2, n[9]*2 + 1))


def tempo(vetor):
    a = []
    b = []
    soma = 0
    somab = 0
    media = 0
    mediab = 0
    for i in range(tamanho_random):
        inicial = time.time()
        insertionsort(vetor)
        final = time.time()
        a.append(final-inicial)

        inicial = time.time()
        mergesort(vetor, 0, len(vetor) -1)
        final = time.time()
        b.append(final - inicial)

    for i in range(len(a)):
        soma += a[i]
        somab += b[i]

        media = soma / tamanho_random
        mediab = somab / tamanho_random

    return [len(vetor), media, mediab]


array = []
for aux in range(10):
   array.append(tempo(vetor[aux]))

df2 = pd.DataFrame(array, columns=  ['tamanho', 'mediaIS', 'mediaMS'])

with plt.style.context('Solarize_Light2'):
    colors = ['b', 'r']
    insort = plt.scatter(df2.tamanho, df2.mediaIS, label='InsertionSort', color=colors[0])
    mgsort = plt.scatter(df2.tamanho, df2.mediaMS, label='MergeSort', color=colors[1])
    plt.title('Comparação do tempo de execução do Insertion Sort vs Merge Sort')
    plt.xlabel('Tamanho de entrada', fontsize=14)
    plt.ylabel('Tempo de execução μs)', fontsize=14)
    plt.legend((insort, mgsort),
               ('Insertion Sort', 'Merge Sort'),
               scatterpoints=1,
               loc='upper left',
               ncol=3,
               fontsize=8)
plt.show()
