from multiprocessing import Pool, cpu_count


def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return merge(esquerda, direita)


def merge_sort_worker(sublista):
    from .mergesort import merge_sort

    return merge_sort(sublista)


def merge_sort_parallel(lista):
    n_cpu = cpu_count()
    tamanho = len(lista)
    tamanho_sublista = tamanho // n_cpu

    sublistas = [
        lista[i * tamanho_sublista : (i + 1) * tamanho_sublista] for i in range(n_cpu)
    ]
    if len(lista) % n_cpu != 0:
        sublistas[-1].extend(lista[n_cpu * tamanho_sublista :])

    with Pool(processes=n_cpu) as pool:
        sublistas_ordenadas = pool.map(merge_sort_worker, sublistas)

    while len(sublistas_ordenadas) > 1:
        novas = []
        for i in range(0, len(sublistas_ordenadas), 2):
            if i + 1 < len(sublistas_ordenadas):
                novas.append(merge(sublistas_ordenadas[i], sublistas_ordenadas[i + 1]))
            else:
                novas.append(sublistas_ordenadas[i])
        sublistas_ordenadas = novas

    return sublistas_ordenadas[0]
