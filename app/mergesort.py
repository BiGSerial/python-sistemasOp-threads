from multiprocessing import Pool, cpu_count, Queue, Process


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


def merge_sort_parallel_improved(lista, threshold=10000):
    """
    Implementação melhorada de merge sort paralelo usando um pool de processos
    com divisão e conquista mais eficiente.

    Args:
        lista: A lista a ser ordenada.
        threshold: Tamanho da lista abaixo do qual o sort sequencial é usado.
    """
    if len(lista) <= threshold:
        return merge_sort(lista)

    # Determina o número ótimo de divisões com base no CPU
    n_chunks = min(cpu_count(), max(1, len(lista) // threshold))
    chunk_size = len(lista) // n_chunks

    # Divide a lista em chunks de tamanho aproximado
    chunks = []
    for i in range(n_chunks - 1):
        chunks.append(lista[i * chunk_size : (i + 1) * chunk_size])
    chunks.append(
        lista[(n_chunks - 1) * chunk_size :]
    )  # O último chunk pode ser um pouco maior

    # Usa um pool de processos para ordenar os chunks em paralelo
    with Pool(processes=n_chunks) as pool:
        sorted_chunks = pool.map(merge_sort, chunks)

    # Combina os chunks ordenados usando uma estratégia de árvore binária
    while len(sorted_chunks) > 1:
        next_level = []
        # Processa pares de chunks em cada nível
        for i in range(0, len(sorted_chunks), 2):
            if i + 1 < len(sorted_chunks):
                next_level.append(merge(sorted_chunks[i], sorted_chunks[i + 1]))
            else:
                next_level.append(sorted_chunks[i])
        sorted_chunks = next_level

    return sorted_chunks[0]


# Função para ler arquivo (mantida do código original)
def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r") as f:
        return [int(linha.strip()) for linha in f if linha.strip()]
