from multiprocessing import Process
import time
import math


def calcular_operacao_intensiva(n):
    for _ in range(100):
        resultado = math.factorial(30000)
    print(f"Processo {n} completou operações intensivas")


if __name__ == "__main__":

    inicio_paralelo = time.perf_counter()

    p1 = Process(target=calcular_operacao_intensiva, args=(1,))
    p2 = Process(target=calcular_operacao_intensiva, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    fim_paralelo = time.perf_counter()
    print(f"Tempo paralelo: {fim_paralelo - inicio_paralelo} segundos")
    # Versão sequencial
    inicio_sequencial = time.perf_counter()
