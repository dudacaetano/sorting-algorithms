
'''funcionalidade: Bubble sort é o algoritmo mais simples, mas o menos eficientes. Neste algoritmo cada elemento da posição i será comparado com o elemento da posição i + 1,
ou seja, um elemento da posição 2 será comparado com o elemento da posição 3. Caso o elemento da posição 2 for maior que o da posição 3, eles trocam de lugar e assim sucessivamente.
Por causa dessa forma de execução, o vetor terá que ser percorrido quantas vezes que for necessária, tornando o algoritmo ineficiente para listas muito grandes'''

#implementação da função que faz a ordenação dos elementos com o conceito do bubble sort
# o algoritmo em questão é de ordem de O(n^2)

#bibliotecas utilizadas
import numpy as np
import matplotlib.pyplot as plt
import time

tamanho_array = 10

array_inicio = np.random.randint(5000,50000,tamanho_array) #definir a partir de onde começa a contagem dos numeros aleatorios
n = len(array_inicio)

print("Array que será ordenado",array_inicio)
print("tamanho do array",n)

array_bubble = array_inicio.copy()
def bubble_sort(array_bubble):

    for i in range(n):
        for j in range(n-i-1):
            if array_bubble[j] > array_bubble[j+1]:
               array_bubble[j], array_bubble[j+1] = array_bubble[j+1], array_bubble[j]
    return array_bubble

array_desordenado = np.copy(array_bubble)
array_ordenado = bubble_sort(array_bubble)

print('O tamanho do array que será ordenado é de:%d posicões '%n)
print("Array que será ordenado",array_desordenado)
print('Array ordenado pelo bubble sort ', array_ordenado)
