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
		self.design_shield = [["|","O","|","#"],[" ","|"," ","#"],["|"," ","|","#"]]
		self.lives = 5
		self.coins = 0
		self.shield = 0 

	
	def initial_placement(self,grid): 

		for i in range(25,28):
			for j in range(0,3):
				grid[i][j] = self.design[i-25][j]

	def disappear_mandalorian(self,grid):
		if self.shield == 0:
			for i in range(self.r,self.r+3):
				for j in range(self.c,self.c+3):
					grid[i][j] = " "
		
		elif self.shield == 1:
			for i in range(self.r,self.r+3):
				for j in range(self.c,self.c+4):
					grid[i][j] = " "			

	def reappear_mandalorian(self,grid):
		if self.shield == 0:
			for i in range(self.r,self.r+3):
				for j in range(self.c,self.c+3):
					grid[i][j] = self.design[i-self.r][j-self.c]
		
		if self.shield == 1:
			for i in range(self.r,self.r+3):
				for j in range(self.c,self.c+4):
					grid[i][j] = self.design_shield[i-self.r][j-self.c]				

	def check_coin_collision(self,grid):
		if self.shield == 0:
			for i in range(self.r,self.r+3):
				for j in range(self.c,self.c+3):
					if grid[i][j] == '$':
						self.coins = self.coins + 1

		if self.shield == 1:
			for i in range(self.r,self.r+3):
				for j in range(self.c,self.c+4):
					if grid[i][j] == '$':
						self.coins = self.coins + 1	

	def check_obstacle_collision(self,grid,start,rows):
		if self.shield == 0:
			for i in range(self.r,self.r+3):
				for j in range(self.c,self.c+3):
					if grid[i][j] == '*':
						self.lives = self.lives - 1
						for ii in range(rows-1):
							for jj in range(start,141+start):
								if grid[ii][jj] == '*':
									grid[ii][jj] = ' '
					break			


		# if self.shield == 1:
			# for i in range(self.r,self.r+3):
				# for j in range(self.c,self.c+4):
					# if grid[i][j] == '*':
						# self.lives = self.lives - 1
																	 

																

