import os
import time
import multiprocessing
import signal

processes = []

def worker():
    os.system(f"python src/worker.py")

def execute_instances():
    num_processes = 4

    for worker_id in range(num_processes):
        process = multiprocessing.Process(target=worker)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

def signal_handler(signum, frame):
    logger.info(f"Recebido sinal {signum}. Terminando os processos filhos...")

    for process in processes:
        process.terminate()  # Termine os processos filhos
    for process in processes:
        process.join()  # Aguarde o término do processo filho

    logger.info("Processos filhos terminados. Encerrando o programa principal.")
    exit(0)

if __name__ == "__main__":
    try:
        execute_instances()
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)
