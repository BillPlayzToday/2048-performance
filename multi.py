import game

def new_game(result_queue):
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
                    "score": current_game.score
                })
                break