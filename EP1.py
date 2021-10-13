import time
from random import sample

'''Algoritmos de ordenação utilizados'''

def quicksort(v):
  if len(v) <= 1: return v
  pivô = v[0]
  iguais  = [x for x in v if x == pivô]
  menores = [x for x in v if x < pivô]
  maiores = [x for x in v if x > pivô]
  return quicksort(menores) + iguais + quicksort(maiores)

def mergesort(v):
    if len(v) <= 1: return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def selection(v):
  r = []
  while v:
    m = min(v)
    r.append(m)
    v.remove(m)
  return r

'''Declaração dos vetores'''

vetor = []            # armazenar os vetores aleatórios a serem ordenados
elementos = []        # armazenar a quantidade de elementos no vetor em cada passo
time_mergesort = []   # armazenar os tempos de cada ordenação, separado em listas para cada algoritmo.
time_quicksort = []
time_native = []
time_selection = []

total_time_start = time.time()       # inicio do timer de tempo total de execução

for elemento in range(2000, 24000, 2000):

    elementos.append(str(elemento))
    vetor += sample(range(elemento), elemento)    # Gerar vetores aleatórios, começando com 2000 e incrementando 2000 elementos a cada passo

    '''Mergesort'''
    inicio = time.time()    #inicio do timer de tempo de execução do algoritmo.
    mergesort(vetor)        #executar algoritmo "Mergesort" de ordenação
    fim = time.time()       #fim do timer de tempo de execução do algoritmo
    time_mergesort += [fim-inicio]    # Resultado do tempo de execução

    '''Quicksort'''
    inicio = time.time()
    quicksort(vetor)
    fim = time.time()
    time_quicksort += [fim-inicio]

    '''Nativo'''
    inicio = time.time()
    sorted(vetor)
    fim = time.time()
    time_native += [fim - inicio]

    '''Selection'''
    inicio = time.time()
    selection(vetor)
    fim = time.time()
    time_selection += [fim-inicio]

total_time_final = time.time()     # Fim do timer de tempo de execução total
total_time = total_time_final - total_time_start


'''Exibição dos Resultados Obtidos'''

print('')
print('-' * 67)
print(f'Total time: {total_time:.2f}s               Time(s)                          |')
print('-' * 67)
print('Nº elementos |  Native   | Quicksort   | Mergesort   | Selection  |')
for linha in range(0, 11):
    if len(elementos[linha]) == 4:
        print(f'{elementos[linha]}' + '         |   ' + f'{time_native[linha]:.3f}' + '   |     ' + f'{time_quicksort[linha]:.3f}' + '   |     ' + f'{time_mergesort[linha]:.3f}' + '   |     ' + f'{time_selection[linha]:.3f}' + '  |')
    else:
        print(f'{elementos[linha]}' + '        |   ' + f'{time_native[linha]:.3f}' + '   |     ' + f'{time_quicksort[linha]:.3f}' + '   |     ' + f'{time_mergesort[linha]:.3f}' + '   |     ' + f'{time_selection[linha]:.3f}' + '  |')
print('-' * 67)