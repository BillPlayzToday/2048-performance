import time
import multiprocessing
import json

import multi

process_queue = multiprocessing.Queue()
max_number = None
max_score = -1
total_games = 0
active_processes = []

def terminate():
    global active_processes
    clear_terminal()
    print("[INFO] Terminating active_processes")
    for process in active_processes:
        process.terminate()
        process.join()
    print("[OK] Terminated active_processes, waiting for loop end.")
    active_processes = []

def clear_terminal():
    print("\033[H\033[J", end="")

def get_max_number(history):
    return max(history[len(history) - 1]["state"].flatten())

for process_id in range(multiprocessing.cpu_count() - 1):
    new_process = multiprocessing.Process(
        target = multi.new_game,
        args = [process_queue]
    )
    active_processes.append(new_process)
    new_process.start()
start_time = time.time()
try:
    while True:
        if (process_queue.empty() and (len(active_processes) == 0)):
            break
        while (not process_queue.empty()):
            queue_item = process_queue.get()
            if ((not max_number) or (get_max_number(max_number) < get_max_number(queue_item["history"]))):
                max_number = queue_item["history"]
            max_score = max(queue_item["score"],max_score)
            total_games = (total_games + 1)
        actual_max_number = max_number
        if (actual_max_number):
            actual_max_number = get_max_number(actual_max_number)
        else:
            actual_max_number = 0
        final_string = f"Games per second: {str(total_games / (time.time() - start_time))}\nMax number: {str(2 ** actual_max_number)}\nMax score: {str(max_score)}\nTotal: {str(total_games)}"
        clear_terminal()
        print(final_string)
except KeyboardInterrupt:
    terminate()
print("[OK] End of loop.")
print(f"Best result: {-1}") # TODO add result string to use for web interface