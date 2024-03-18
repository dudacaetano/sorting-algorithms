'''funcionalidade:Um número a partir do primeiro, este número escolhido é comparado com os números a partir da sua direita, quando encontrado 
um número menor, o número escolhido ocupa a posição do menor número encontrado. Este número encontrado será o próximo número escolhido, 
caso não for encontrado nenhum número menor que este escolhido, ele é colocado na posição do primeiro número escolhido, 
e o próximo número à sua direita vai ser o escolhido para fazer as comparações. É repetido esse processo até que a lista esteja ordenada'''

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
# algoritmo de ordenação select sort

array_select = array_inicio.copy()
def select_sort(array_select):
   for i in range(n-1):
      minimum = i
      for j in range(i+1,n):
          if array_select[j] < array_select[minimum]:
             minimum = j
      array_select[i] , array_select[minimum] = array_select[minimum], array_select[i]
   return array_select

array_desordenado = np.copy(array_select)
array_ordenado = select_sort(array_select)

print('O tamanho do array que será ordenado é de:%d posicões '%n)
print("Array que será ordenado",array_desordenado)
print('Array ordenado pelo select sort ', array_ordenado)