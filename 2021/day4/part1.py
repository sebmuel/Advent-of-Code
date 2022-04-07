def remove_whitespace(liste):
    j = []
    for liste in liste:
        h = []
        for str in liste:
            h.append(str.strip())
        j.append(h)
    return j


with open("input.in") as fin:
    holder = []
    holderA = []
    numbers = fin.readline().strip("\n")
    numbers = numbers.split(",")
    next(fin)
    boardData = [i for i in fin.read().split("\n")]
    boardData = list(filter(None, boardData))
    for board in boardData:
        holder.append([board[i:i + 3] for i in range(0, len(board), 3)])
    final = remove_whitespace(holder)
    boards = ([final[i:i + 5] for i in range(0, len(final), 5)])


class Game:
    boards_left = 101

    def minus(self):
        self.boards_left = self.boards_left - 1


class Board:
    row = 0
    column = 0
    flag = True

    def __init__(self, list):
        self.board = list

    def calcb(self, board_to_calc, num):
        left_numbers = 0
        for b in board_to_calc:
            for x in b:
                if x != "hit":
                    left_numbers = int(left_numbers + int(x))
        print(left_numbers * int(num))

    def round(self, number):
        for i, b in enumerate(self.board):
            for z, c in enumerate(b):
                if c == number:
                    b[z] = "hit"
                    if self.count_columns(self.board) and self.flag:
                        self.flag = False
                        game_round.minus()
                        if game_round.boards_left == 1:
                            self.calcb(self.board, number)
                            return True
                    if self.count_rows(self.board) and self.flag:
                        self.flag = False
                        game_round.minus()
                        if game_round.boards_left == 1:
                            self.calcb(self.board, number)
                            return True

    def count_columns(self, matrix):
        column_count = len(matrix)
        column_index = 0
        count_hits = 0
        while column_count > 0:
            for column in matrix:
                if column[column_index] == "hit":
                    count_hits = count_hits + 1
                if count_hits == 5:
                    return True
            column_count = column_count - 1
            column_index = column_index + 1
            count_hits = 0

    def count_rows(self, matrix):
        row_hits = 0
        for i, b in enumerate(matrix):
            for z, c in enumerate(b):
                if b[z] == "hit":
                    row_hits = row_hits + 1
                if row_hits == 5:
                    return True
            row_hits = 0


objs = [Board(i) for i in boards]
game_round = Game()

print(len(objs))

def play(er):
    for num in er:
        print(game_round.boards_left)
        for obj in objs:

            if obj.round(num):
                print("w")



play(numbers)
