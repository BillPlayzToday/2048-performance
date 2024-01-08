import time
import multiprocessing

import multi

buffer_length = 4096

process_queue = multiprocessing.Queue()
max_number = -1
max_score = -1
total_games = 0

def clear_terminal():
    print("\033[H\033[J", end="")

for process_id in range(multiprocessing.cpu_count() - 1):
    new_process = multiprocessing.Process(
        target = multi.new_game,
        args = [process_queue]
    )
    new_process.start()
start_time = time.time()
while True:
    while (not process_queue.empty()):
        queue_item = process_queue.get()
        max_number = max(queue_item["number"],max_number)
        max_score = max(queue_item["score"],max_score)
        total_games = (total_games + 1)

    final_string = f"Games per second: {str(total_games / (time.time() - start_time))}\nMax number: {str(2 ** max_number)}\nMax score: {str(max_score)}\nTotal: {str(total_games)}"
    clear_terminal()
    print(final_string)