from multiprocessing import Process
import time


def tarefa_demorada():
    print("Iniciando tarefa...")

    time.sleep(2)
    fim = int(time.time() * 1000)  # Unix time em milissegundos

    print(f"Tarefa concluída - Timestamp: {fim}")


def tarefa_demorada2():
    print("Iniciando tarefa...")

    time.sleep(3)
    fim = int(time.time() * 1000)  # Unix time em milissegundos

    print(f"Tarefa concluída - Timestamp: {fim}")


if __name__ == "__main__":
    processo1 = Process(target=tarefa_demorada2)
    processo2 = Process(target=tarefa_demorada)

    processo1.start()
    processo2.start()

    processo1.join()
    processo2.join()

    print("Todos os processos finalizados.")
