# import os
# from .leitura import ler_arquivo
# from .mergesort import merge_sort, merge_sort_parallel


# def medir_tempo(funcao, lista):
#     import time

#     inicio = time.perf_counter()
#     funcao(lista.copy())
#     fim = time.perf_counter()
#     return (fim - inicio) * 1000  # milissegundos


# def executar_testes_em_pasta(pasta):
#     tempos_seq = []
#     tempos_par = []
#     nomes_arquivos = []

#     arquivos_txt = [f for f in os.listdir(pasta) if f.endswith(".txt")]

#     arquivos_ordenados = sorted(arquivos_txt, key=lambda x: int(os.path.splitext(x)[0]))

#     for arquivo in arquivos_ordenados:
#         caminho = os.path.join(pasta, arquivo)
#         dados = ler_arquivo(caminho)

#         nome_base = os.path.splitext(arquivo)[0]  # Remove .txt
#         nomes_arquivos.append(nome_base)

#         t_seq = [medir_tempo(merge_sort, dados) for _ in range(10)]
#         t_par = [medir_tempo(merge_sort_parallel, dados) for _ in range(10)]

#         tempos_seq.append(t_seq)
#         tempos_par.append(t_par)

#     return tempos_seq, tempos_par, nomes_arquivos

import os
from .leitura import ler_arquivo
from .mergesort import (
    merge_sort,
    merge_sort_parallel,
    merge_sort_forkjoin,
)  # Importa o novo método


def medir_tempo(funcao, lista):
    import time

    inicio = time.perf_counter()
    funcao(lista.copy())
    fim = time.perf_counter()
    return (fim - inicio) * 1000  # milissegundos


def executar_testes_em_pasta(pasta, parallel_type="process_pool"):
    """
    Executa testes em uma pasta, medindo tempos sequenciais e paralelos.

    Args:
        pasta: Caminho da pasta contendo os arquivos de teste.
        parallel_type: 'process_pool' para o método original ou 'fork_join' para o novo.
    """
    tempos_seq = []
    tempos_par = []
    nomes_arquivos = []

    arquivos_txt = [f for f in os.listdir(pasta) if f.endswith(".txt")]

    arquivos_ordenados = sorted(arquivos_txt, key=lambda x: int(os.path.splitext(x)[0]))

    for arquivo in arquivos_ordenados:
        caminho = os.path.join(pasta, arquivo)
        dados = ler_arquivo(caminho)

        nome_base = os.path.splitext(arquivo)[0]  # Remove .txt
        nomes_arquivos.append(nome_base)

        t_seq = [medir_tempo(merge_sort, dados) for _ in range(10)]
        if parallel_type == "process_pool":
            t_par = [
                medir_tempo(merge_sort_parallel, dados) for _ in range(10)
            ]  # Método original
        elif parallel_type == "fork_join":
            t_par = [
                medir_tempo(merge_sort_forkjoin, dados) for _ in range(10)
            ]  # Novo método
        else:
            raise ValueError(f"Tipo de paralelismo inválido: {parallel_type}")

        tempos_seq.append(t_seq)
        tempos_par.append(t_par)

    return tempos_seq, tempos_par, nomes_arquivos
