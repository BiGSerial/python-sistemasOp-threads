from multiprocessing import Process
import time

def tarefa_demorada():
    print("Iniciando tarefa...")
    time.sleep(1)
    print("Tarefa concluída.")

if __name__ == "__main__":
    processo1 = Process(target=tarefa_demorada)
    processo2 = Process(target=tarefa_demorada)

    processo1.start()
    processo2.start()
    
    processo1.join()
    processo2.join()

    print("Todos os processos finalizados.")
