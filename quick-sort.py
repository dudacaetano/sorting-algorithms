'''Funcionalidade:Segue uma abordagem de divisão e conquista, onde escolhe em elemento do array para utilizar de pivô
que servirá para dividir o array e sublista de elemento maior e menor do que o pivô,
fazendo chamadas recursivas das sublistas dos elementos maiores e menores que o pivô.'''

#bibliotecas utilizadas
import numpy as np
import matplotlib.pyplot as plt
import time

tamanho_array = 10

array_inicio = np.random.randint(5000,50000,tamanho_array) #definir a partir de onde começa a contagem dos numeros aleatorios
n = len(array_inicio)

print("Array que será ordenado",array_inicio)
print("tamanho do array",n)

#o algoritmo em questão é de orddem de O(nlogn)
#algoritmo de ordenação quick sort

array_quick = array_inicio.copy()
def quick_sort(array_quick):
    if len(array_quick) <= 1:
        return array_quick

    pivo = array_quick[0]
    #print("pivo:",pivo)
    lista_direita = []
    lista_esquerda = []

    for i in range(1, len(array_quick)):
        if array_quick[i] >= pivo:
            lista_direita.append(array_quick[i])
        else:
            lista_esquerda.append(array_quick[i])

    lista_direita_ordenada = quick_sort(lista_direita)
    lista_esquerda_ordenada = quick_sort(lista_esquerda)

    array_inicio_ordenado = lista_esquerda_ordenada + [pivo] + lista_direita_ordenada

    return array_inicio_ordenado

array_desordenado = np.copy(array_quick)
array_ordenado = quick_sort(array_quick)

print("Array desordenado:", array_desordenado)
print('Array ordenado pelo quick sort:', array_ordenado)

