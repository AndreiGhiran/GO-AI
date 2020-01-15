import numpy as np

BLACK = 1
EMPTY = 0
WHITE = -1

class Game:

    def __init__(self):
        self.boardSize = 19
        self.board = np.zeros((self.boardSize+2,self.boardSize+2),dtype= "int16")
        self.komi = 6.5
        self.blackScore = 0
        self.whiteScore = 0

    def printBoard(self):
        for x in range(1,self.boardSize + 1):
            for y in range(1,self.boardSize + 1):
                print(str(self.board[x][y]) + " ",end="")
            print("\n")
    
    def changeBoardSize(self,newBoardSize):
        self.boardSize = newBoardSize;

    def changeKomi(self,newKomiValue):
        self.komi = newKomiValue

    def addWhiteScore(self,value):
        self.whiteScore = self.whiteScore + value

    def addBlackScore(self,value):
        self.blackScore = self.blackScore + value

    def getWhiteScore(self):
        return self.whiteScore
    
    def getBlackScore(self):
        return self.blackScore
    
    def isMoveValid(self,x,y):
        if x >= 0 and y >= 0 and x < self.boardSize and y < self.boardSize:
            if self.board[x][y] == 0:
                return True
        return False

    def makeMove(self,x,y,color):
        if self.isMoveValid(x,y):
            self.board[x][y] = color
        else:
            return False

    def removeCapturedStones(self,color):
        color = -color
        for x in range(1,self.boardSize + 1):
            for y in range(1,self.boardSize + 1):
                if self.board[x-1][y] == self.board[x][y-1] == self.board[x+1][y] == self.board[x][y+1] == color:
                    if color == BLACK:
                        self.addWhiteScore(1)
                        self.board[x][y] = 0
                    else:
                        self.addBlackScore(1)
                        self.board[x][y] = 0
                elif self.board[x-1][y] == 0 or self.board[x+1][y] == 0 or self.board[x][y-1] == 0 or self.board[x][y+1] == 0:
                    continue
                elif 

    

da = Game()
da.printBoard()