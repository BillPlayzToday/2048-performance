import time
import random
import numpy
import io
import struct

import game

buffer_length = 4096

last_game_over = None
games_per_second = io.BytesIO()
max_score = -1

def clear_terminal():
    print("\033[H\033[J", end="")

def get_average():
    cursor_before = games_per_second.tell()
    games_per_second.seek(0)

    unpacked_array = []
    while True:
        read_bytes = games_per_second.read(4)
        if (len(read_bytes) != 4):
            break
        unpacked_array.append(struct.unpack(">i",read_bytes))
    
    games_per_second.seek(cursor_before)
    return numpy.average(unpacked_array)

while True:
    current_game = game.game2048()
    while True:
        swipe_return = random.choice([current_game.swipe_up,current_game.swipe_right,current_game.swipe_down,current_game.swipe_left])()
        if (not swipe_return):
            current_score = max(current_game.state.flatten())
            max_score = max(max_score,current_score)
            break
    current_time = time.time()
    if (last_game_over):
        games_per_second.write(struct.pack(">i",round(1 / (current_time - last_game_over))))
        if (games_per_second.tell() == buffer_length):
            games_per_second.seek(0)
    last_game_over = current_time

    clear_terminal()
    print(f"Games per second: {str(get_average())}")
    print(f"Max score: {str(2 ** max_score)}")
    print(f"Cursor: {str(games_per_second.tell())}")