import copy
import time


class Queens:
    def __init__(self, size):
        self.size = size
        self.combinations = []

    @staticmethod
    def get_address(cell):
        return ord(cell[0])-97, int(cell[1:])-1

    @staticmethod
    def get_name(address):
        return chr(address[0] + 97) + str(address[1] + 1)

    @staticmethod
    def select_row(number, board):
        symbol = chr(number + 97)
        row = []
        for cell in board:
            if symbol in cell:
                row.append(cell)
        return row

    @staticmethod
    def generate_board(size):
        board = []
        for x in range(size):
            for y in range(size):
                board.append(Queens.get_name((x, y)))
        return board

    @staticmethod
    def delete_cell(name, board):
        if name in board:
            board.remove(name)

    def prune(self, start, initial_board):
        board = copy.deepcopy(initial_board)
        x, y = Queens.get_address(start)
        # horizontal
        for i in range(self.size):
            Queens.delete_cell(Queens.get_name((x, i)), board)
        # vertical
        for i in range(self.size):
            Queens.delete_cell(Queens.get_name((i, y)), board)
        # forward diagonal
        # down
        for i in range(1, min(x, y) + 1):
            Queens.delete_cell(Queens.get_name((x - i, y - i)), board)
        # up
        for i in range(1, self.size - max(x, y)):
            Queens.delete_cell(Queens.get_name((x + i, y + i)), board)
        # backward diagonal
        # down
        for i in range(1, min(self.size - x, y) + 1):
            Queens.delete_cell(Queens.get_name((x + i, y - i)), board)
        # up
        for i in range(1, min(x, self.size - y) + 1):
            Queens.delete_cell(Queens.get_name((x - i, y + i)), board)
        return board

    # def remove_symmetrical(start, initial_board):
    #     board = copy.deepcopy(initial_board)
    #     x, y = get_address(start)
    #     delete_cell(get_name((x, y)), board)
    #     delete_cell(get_name((size - 1 - x, size - 1 - y)), board)
    #     delete_cell(get_name((y, x)), board)
    #     delete_cell(get_name((size - 1 - y, size - 1 - x)), board)
    #     delete_cell(get_name((size - 1 - x, y)), board)
    #     delete_cell(get_name((size - 1 - y, x)), board)
    #     delete_cell(get_name((y, size - 1 - x)), board)
    #     delete_cell(get_name((x, size - 1 - y)), board)
    #     return board

    def generate_queens(self):
        board = Queens.generate_board(self.size)
        self.backtrack(0, board, '')

    def backtrack(self, queen, initial_board, initial_locations):
        locations = initial_locations
        if initial_board:
            row = Queens.select_row(queen, initial_board)
            if row:
                for cell in row:
                    board = self.prune(cell, initial_board)
                    self.backtrack(queen + 1, board, locations + '-' + cell + ',')
            else:
                self.backtrack(queen + 1, [], '')
        else:
            if queen == self.size:
                self.combinations.append(locations)


if __name__ == '__main__':
    size = 10
    game = Queens(size)

    start_time = time.time()
    game.generate_queens()
    print(game.combinations)
    print("Combinations: {}".format(len(game.combinations)))
    print("Time of execution: {:.2f}".format(time.time() - start_time))
