'''funcionalidade: Segue a mesma abordagem do quick sort.Ele divide a lista de elementos em sub-listas contendo, 
ordena as lista individualmente e depois mescla as duas ordenando de maneira recursiva.

obs: curiosidade , o python possui uma função nativa chamada Sorted() que implementa ordenção merge sort por padrão'''


#bibliotecas utilizadas
import numpy as np
import matplotlib.pyplot as plt
import time

tamanho_array = 10

array_inicio = np.random.randint(5000,50000,tamanho_array) #definir a partir de onde começa a contagem dos numeros aleatorios
n = len(array_inicio)

print("Array que será ordenado",array_inicio)
print("tamanho do array",n)

# Implementação do algoritmo de ordenação merge sort
# O algoritmo em questão é da ordem de O(nlogn) em todos os casos

array_merge = array_inicio.copy()
def merge_sort (array_merge):

    if len(array_merge) <= 1:
        return array_merge
    
    meio = len(array_merge) //2 
    resultado = []
    
    direita = merge_sort(array_merge[:meio])
    esquerda = merge_sort(array_merge[meio:])

    i=j=0

    for _ in range ( len(array_merge)):

       if i < len(esquerda) and (j>= len(direita) or esquerda[i] < direita[j]):
             resultado.append(esquerda[i])
             i += 1
       else:
             resultado.append(direita[j])
             j+=1
        
            

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])


    return resultado

array_desordenado = np.copy(array_merge)
array_ordenado = merge_sort(array_merge)

print("Array desordenado:", array_desordenado)
print('Array ordenado pelo merge sort:', array_ordenado)


