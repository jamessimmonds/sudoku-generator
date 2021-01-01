from solver import Solver

class Generator():

    def __init__(self):

        sudoku_row = ['0' for x in range(0, 9)]
        self.grid = [sudoku_row.copy() for x in range(0, 9)]

        s = Solver()
        s.solve(self.grid)

if __name__ == "__main__":

    g = Generator()
    print(g.grid)