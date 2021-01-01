import random

class Solver():

    def is_solved(self, grid):
        for row in grid:
            if "0" in row:
                return False
        return True

    def next_unsolved(self, grid):
        for row in range(0, 9):
            for col in range(0, 9):
                if grid[row][col] == "0":
                    return (row, col)
        return None

    def test_insertion_row(self, grid, row, candidate):
        if str(candidate) not in grid[row]:
            return True
        else:
            return False

    def test_insertion_col(self, grid, col, candidate):
        house = []

        for row in grid:
            house.append(row[col])

        if str(candidate) not in house:
            return True
        else:
            return False

    def test_insertion_box(self, grid, row, col, candidate):
        house = []

        for row_index in range(0, 9):
            for col_index in range(0, 9):
                if row_index // 3 == row // 3 and col_index // 3 == col // 3:
                    house.append(grid[row_index][col_index])

        if str(candidate) not in house:
            return True
        else:
            return False

    def test_insertion(self, grid, row, col, candidate):
        if self.test_insertion_row(grid, row, candidate) and self.test_insertion_col(grid, col, candidate) and self.test_insertion_box(grid, row, col, candidate):
            return True
        else:
            return False   

    def solve(self, grid, candidates=[1,2,3,4,5,6,7,8,9]):

        if self.is_solved(grid):
            return True

        row, col = self.next_unsolved(grid)

        for candidate in candidates:
            if self.test_insertion(grid, row, col, candidate):

                grid[row][col] = str(candidate)
                if self.solve(grid, candidates):
                    return True
            else:
                grid[row][col] = "0"
            
        return False

if __name__ == "__main__":

    raw_input = """003020600
    900305001
    001806400
    008102900
    700000008
    006708200
    002609500
    800203009
    005010300"""

    input_lines = raw_input.split("\n")

    sudoku = []

    for line in input_lines:
        stripped_line = [character for character in line if character != " "]
        sudoku.append(stripped_line)

    s = Solver()
    print(s.solve(sudoku))
    print(sudoku)