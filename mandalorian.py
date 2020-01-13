from colorama import init, Fore
init()
import os

class person:
	def __init__(self,r,c):
		self.r = r
		self.c = c

class mandalorian(person):
	def __init__(self,r,c):
		person.__init__(self,r,c)
		self.design = [["|","O","|"],[" ","|"," "],["|"," ","|"]]
		self.lives = 5
		self.coins = 0

	
	def initial_placement(self,grid): 

		for i in range(25,28):
			for j in range(0,3):
				grid[i][j] = self.design[i-25][j]

	def disappear_mandalorian(self,grid):
		for i in range(self.r,self.r+3):
			for j in range(self.c,self.c+3):
				grid[i][j] = " "

	def reappear_mandalorian(self,grid):
		for i in range(self.r,self.r+3):
			for j in range(self.c,self.c+3):
				grid[i][j] = self.design[i-self.r][j-self.c]											

