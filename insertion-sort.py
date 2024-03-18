
'''funcionalidade:Percorre uma lista de elementos, inserindo cada elemento na posição correta em relação aos elementos já ordenados. 
Começa pelo segundo elemento da lista comparando ele com o primeiro elemento da lista. Avança para a esquerda enquanto o elemento for 
menor que os elementos que está sendo comparado até que ele seja maior ou igual, então segue para o próximo da lista, 
até que toda a lista esteja ordenada'''
#bibliotecas utilizadas
import numpy as np
import matplotlib.pyplot as plt
import time

tamanho_array = 10

array_inicio = np.random.randint(5000,50000,tamanho_array) #definir a partir de onde começa a contagem dos numeros aleatorios
n = len(array_inicio)

print("Array que será ordenado",array_inicio)
print("tamanho do array",n)


#o algoritmo em questão é de ordem de O(n^2)
# algoritmo de ordenação insertion sort

array_insertion = array_inicio.copy()
def insertion_sort(array_insertion):

  for i in range(1,n):
    for j in range(i, 0 , -1):

      if array_insertion[j] >= array_insertion[j-1]:
        break

      array_insertion[j], array_insertion[j-1] = array_insertion[j-1], array_insertion[j]

  return array_insertion

array_desordenado = np.copy(array_insertion)
array_ordenado = insertion_sort(array_insertion)

print('O tamanho do array que será ordenado é de:%d posicões '%n)
print("Array que será ordenado", array_desordenado)
print('Array ordenado pelo insertion sort ', array_ordenado)
