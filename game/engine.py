import random
import numpy as np

class Engine:

	def __init__(self):
		self.boardsize = 19
		self.board =  np.zeros((self.boardsize,self.boardsize))
	def go_protocol_version(self):
		return "= 1.0\n"
	
	def go_name(self):
		return "= SomeAI\n"

	def go_version(self):
		return "= 1.0\n"
	
	def go_known_commands(self,command_name):
		return "go_"+command_name in dir(self) + "\n"

	def go_list_commands(self):
		listaComenzi = []
		print(dir(self))
		for x in dir(self):
			if x[0:3] == "go_":
				listaComenzi.append(x[3:])
		
		return "= " + "\n".join(listaComenzi) +"\n"
	
	def go_quit(self):
		exit()

	def go_komi(self,amount):
		self.komi = amount
		return "= none\n"
	
	def go_boardsize(self,size):
		self.boardsize = int(size)
		self.board =  np.zeros((self.boardsize,self.boardsize))
		return "= none\n"

	def go_clear_board(self):
		#clear board
		return "= none\n"
	
	def go_play(self,*color):
		a = "A"
		if color[0] == "B":
			self.board[int(color[1][1:])][ord(color[1][0])-ord(a)] = 1
		else:
			self.board[int(color[1][1:])][ord(color[1][0])-ord(a)] = -1
		return "= none\n"

	def go_genmove(self,color):
		lista = []
		a = "A"
		for x in range(0,self.boardsize):
			lista.append(chr(ord(a) + x))
		line = random.choice(lista)
		column = str(random.randint(0,self.boardsize-1))
		while self.board[int(column),ord(line)-ord(a)] != 0:
			line = random.choice(lista)
			column = str(random.randint(0,self.boardsize-1))
		if color == "B":
			self.board[int(column),ord(line)-ord(a)] = 1
		else:
			self.board[int(column),ord(line)-ord(a)] = -1
		return "= " + line + column + "\n"

game = Engine()

while True:
	command = input()
	command = command.split(" ")
	m = globals()["game"]
	func = getattr(m,"go_"+command[0])
	try:
		if len(command) == 3:
			print(func(command[1],command[2]))
		else:
			print(func(command[1]))
	except:
		print(func())