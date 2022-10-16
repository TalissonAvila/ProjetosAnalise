# Projeto de análise de algoritmos.

Neste projeto você vai comparar dois algoritmos de ordenação. Na comparação, você vai apresentar um gráfico no qual o eixo horizontal representa o tamanho do vetor de entrada e o eixo vertical representa o tempo de execução. Seu código deve escolher aleatoriamente 10 tamanhos de vetores de forma que cada tamanho n seja tal que 10 ≤ n ≤ 10.000.
Para o tempo de execução de cada tamanho de entrada n, você deve executar os algoritmos com m entradas de tamanho n de forma que m é escolhido aleatoriamente tal que 10 ≤ m ≤ 20. O m escolhido aleatoriamente deve ser o mesmo para todos os tamanhos de entrada. Note que, para uma comparação mais justa, todos os algoritmos devem ser executado com o mesmo conjunto de entradas. Além disso, para um vetor de tamanho n, cada um dos seus elementos A[i], para 1 ≤ i ≤ n, deve ser um ponto flutuante escolhido aleatoriamente tal que −2n ≤ A[i] ≤ 2n.


## Com esses parâmentros o código faz:
*	Merge Sort comparado com o Insetion Sort.

### Funcionamento do Insertion Sort
O Insertion Sort é um algoritmo de classificação baseado em comparação local. Nele, um subconjunto do vetor é mantido como ordenado, o qual vai crescendo à medida que o vetor é percorrido e cada elemento é devidamente posicionado. Nesse posicionamento o novo item em foco tem que encontrar seu lugar apropriado e então ser inserido. Dessa característica origina o seu nome Insertion Sort, ou ordenação por inserção.
Em um passo-a-passo, o algoritmo segue as etapas abaixo ao percorrer o vetor:
1. Se for o primeiro elemento, ele já está classificado.
2. Escolha o próximo elemento
3. Compare com todos os elementos na sub-lista classificada
4. Desloque todos os elementos na sub-lista classificada que são maiores que o valor a ser ordenado
5. Insira o valor
6. Repita até que a sub-lista classificada seja toda a lista

#### Na animação abaixo mostra como funciona o insertion sort:
![InsertionSort](https://miro.medium.com/max/720/1*5WXRN62ddiM_Gcf4GDdCZg.gif)

### Funcionamento do Merge Sort
O Merge Sort é um dos algoritmos de classificação mais eficientes. Ele tem como princípio de funcionamento a divisão e conquista. O algoritmo divide repetidamente uma lista em várias sub-listas até que cada sub-lista consista em um único elemento, e ao retornar mesclando essas sub-listas ordenadamente, obtém-se a lista original de forma ordenada. Esse processo pode ser descrito pelos passos a seguir:
1. Se houver apenas 1 elemento na lista, está ordenado, retorne
2. Divida a lista recursivamente ao meio até que não possa ser mais dividida
3. Mescle as listas menores em uma nova lista ordenada

#### Na animação abaixo mostra como funciona o merge sort:
![MergeSort](https://miro.medium.com/max/480/1*mh9np1i9PCF2F-4dSEMKuA.gif)

### Dado os códigos utilizados nesse repositório, utilizando os valores de tamanho a seguir, o Insertion Sort e Merge Sort geram a seguionte média de tempo de execução:

Tamanho de entrada | Média de tempo de execução do Insertion Sort | Média de tempo de execução do Merge Sort
:----------------: | :------------------------------------------: | :--------------------------------------:
970 | 0.004383737390691584 | 0.004609281366521662
7846 | 0.274373704736883 | 0.04347198659723455
8167 | 0.3175910169428045 | 0.05510703000155362
7417 | 0.27507567405700684 | 0.04174631292169744
2585 | 0.030282128940929066 | 0.013100819154219194
2822 | 0.03354432366111062 | 0.014461669054898348
7526 | 0.2546842098236084 | 0.041987614198164505
7942 | 0.27671963518316095 | 0.04425367442044345
3154 | 0.04553443735296076 | 0.01614603129300204
4724 | 0.09845744479786266 | 0.024554057554765182

### Para melhorar a visualição, abaixo tem uma foto do gráfico comparando os algoritmos nesses dez tamanhos de entrada:
![GraficoISxMS](https://raw.githubusercontent.com/TalissonAvila/ProjetosAnalise/grafico/figuraprojeto.png?token=GHSAT0AAAAAABZEJZBZRTONH2GMG6WEGXB4Y2MHGYQ)

__Note que, nesse caso, para o valor de entrada sendo 970, a média de tempo do insertion sort é menor mas, para valores, nesse caso, a partir de 2585, o merge sort tem média de tempo inferior, sendo que, para valores cada vez maior, essa diferença de tempo também aumenta.__

### __Para replicar o código desse repositório, se faz necessário importar as biblioteca python pandas e matplotlib além de ter os algoritmos do insertion sort e do merge sort__
