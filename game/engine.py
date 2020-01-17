import random
import numpy as np


globalLetterDict = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "J": 8,
   "K": 9,
   "L": 10,
   "M": 11,
    "N": 12,
    "O": 13,
    "P": 14,
   "Q": 15,
   "R": 16,
   "S": 17,
    "T": 18,
}


class Engine:
    def __init__(self):
        self.boardsize = 19
        self.board = np.zeros((self.boardsize, self.boardsize))

    def go_protocol_version(self):
        return "= 1.0\n"

    def go_name(self):
        return "= SomeAI\n"

    def go_version(self):
        return "= 1.0\n"

    def go_known_commands(self, command_name):
        return "go_" + command_name in dir(self) + "\n"

    def go_list_commands(self):
        listaComenzi = []
        print(dir(self))
        for x in dir(self):
            if x[0:3] == "go_":
                listaComenzi.append(x[3:])

        return "= " + "\n".join(listaComenzi) + "\n"

    def go_quit(self):
        exit()

    def go_komi(self, amount):
        self.komi = amount
        return "= none\n"

    def go_boardsize(self, size):
        self.boardsize = int(size)
        self.board = np.zeros((self.boardsize, self.boardsize))
        return "= board size changed\n"

    def go_clear_board(self):
        self.board = np.zeros((self.boardsize, self.boardsize))
        return "= board cleared\n"

    def go_play(self, color, move="pass"):
        if move == "pass":
            return "= acknowledged move\n"
        if color == "W":
            self.board[int(move[1:])-1][globalLetterDict[move[0]]] = 1
        else:
            self.board[int(move[1:])-1][globalLetterDict[move[0]]] = -1
        return "= acknowledged move\n"

    def go_genmove(self, color):
        lista = []
        for x in globalLetterDict.keys():
            lista.append(x)
        column = random.choice(lista)
        line = str(random.randint(0, self.boardsize - 1))
        while self.board[int(line), globalLetterDict[column]] != 0:
            column = random.choice(lista)
            line = str(random.randint(0, self.boardsize - 1))
        if color == "W":
            self.board[int(line), globalLetterDict[column]] = 1
        else:
            self.board[int(line), globalLetterDict[column]] = -1
        return "= " + column + str(int(line) + 1) + "\n"


game = Engine()

while True:
    command = input()
    command = command.split(" ")
    m = globals()["game"]
    func = getattr(m, "go_" + command[0])
    try:
        if len(command) == 3:
            print(func(command[1], command[2]))
        else:
            print(func(command[1]))
    except:
        print(func())

