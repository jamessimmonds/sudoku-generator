import random

from solver import Solver

class Generator():

    def __init__(self):

        sudoku_row = ['0' for x in range(0, 9)]
        self.grid = [sudoku_row.copy() for x in range(0, 9)]

        candidates = [1,2,3,4,5,6,7,8,9]
        random.shuffle(candidates)

        s = Solver()
        s.solve(self.grid, candidates)

if __name__ == "__main__":

    g = Generator()
    print(g.grid)