import multiprocessing

import game

def new_game(result_queue):
    try:
        while True:
            current_game = game.game2048()
            while True:
                current_game.swipe_up()
                current_game.swipe_right()
                current_game.swipe_down()
                current_game.swipe_left()
                if (current_game.is_over()):
                    result_queue.put({
                        "number": max(current_game.state.flatten()),
                        "score": current_game.score,
                        "history": current_game.history
                    })
                    break
    except KeyboardInterrupt:
        print(f"[{str(multiprocessing.current_process().ident)} - OK] Stopped process")