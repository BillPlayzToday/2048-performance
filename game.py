import random
import numpy


class game2048:
    def __init__(self,resolution = 4):
        self.resolution = resolution
        self.state = numpy.zeros((resolution,resolution),dtype = numpy.int8)
        for i in range(2):
            self._add_new()

    def _get_free_positions(self):
        free_positions = []
        for y in range(len(self.state)):
            for x in range(len(self.state[y])):
                if (self.state[y,x] == 0):
                    free_positions.append((y,x))
        return free_positions
    
    def _add_new(self):
        free_positions = self._get_free_positions()
        if (free_positions == []):
            return False
        self.state[random.choice(free_positions)] = numpy.random.choice([1,2],p = [0.75,0.25])
        return True

    def swipe_up(self):
        rotated_state = numpy.rot90(self.state,1)
        self.state = numpy.rot90(_swipe(rotated_state),-1)
        return self._add_new()

    def swipe_right(self):
        rotated_state = numpy.rot90(self.state,2)
        self.state = numpy.rot90(_swipe(rotated_state),-2)
        return self._add_new()

    def swipe_down(self):
        rotated_state = numpy.rot90(self.state,-1)
        self.state = numpy.rot90(_swipe(rotated_state),1)
        return self._add_new()

    def swipe_left(self):
        self.state = _swipe(self.state)
        return self._add_new()

    def print(self):
        for row in self.state:
            row_string = " "
            for value in row:
                if (value != 0):
                    print_value = str(2 ** value)
                else:
                    print_value = "X"
                row_string = f"{row_string}{print_value} "
            print(row_string)

def _swipe(field):
    for row_index in range(len(field)):
        row = list(field[row_index])
        stripped_row = []
        for item in row:
            if (item != 0):
                stripped_row.append(item)
        
        index = 0
        while (index < (len(stripped_row) - 1)):
            if (stripped_row[index] == stripped_row[index + 1]):
                stripped_row[index] = (stripped_row[index] + 1)
                del stripped_row[index + 1]
            index = (index + 1)

        while (len(stripped_row) < 4):
            stripped_row.append(0)
        
        field[row_index] = numpy.array(stripped_row,dtype = numpy.int8)
        
    return field
