import multiprocessing
import random

import game

def new_game(result_queue):
    try:
        while True:
            current_game = game.game2048()
            while True:
                strat_circle(current_game)
                # strat_random(current_game)
                if (current_game.is_over()):
                    result_queue.put({
                        "number": max(current_game.state.flatten()),
                        "score": current_game.score,
                        "history": current_game.history
                    })
                    break
    except KeyboardInterrupt:
        print(f"[{str(multiprocessing.current_process().ident)} - OK] Stopped process")

def strat_circle(current_game):
    current_game.swipe_up()
    current_game.swipe_right()
    current_game.swipe_down()
    current_game.swipe_left()

def strat_random(current_game):
    random.choice([current_game.swipe_up,current_game.swipe_right,current_game.swipe_down,current_game.swipe_left])()