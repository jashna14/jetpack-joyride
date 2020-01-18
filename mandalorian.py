from colorama import init, Fore
from grid import *
init()

import os

class person:
	def __init__(self,r,c):
		self._r = r
		self._c = c

class mandalorian(person):
	def __init__(self,r,c):
		person.__init__(self,r,c)
		self.__design = [["|","O","|"],[" ","|"," "],["|"," ","|"]]
		self.__design_shield = [["|","O","|","#"],[" ","|"," ","#"],["|"," ","|","#"]]
		self.__lives = 5
		self.__coins = 0
		self.__shield = 0 

	
	def initial_placement(self,obj_grid): 

		for i in range(25,28):
			for j in range(0,3):
				obj_grid.set_grid(i,j,self.__design[i-25][j])

	def disappear_mandalorian(self,obj_grid):
		if self.__shield == 0:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+3):
					obj_grid.set_grid(i,j," ")
		
		elif self.__shield == 1:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+4):
					obj_grid.set_grid(i,j," ")			

	def reappear_mandalorian(self,obj_grid):
		if self.__shield == 0:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+3):
					obj_grid.set_grid(i,j,self.__design[i-self._r][j-self._c])
		
		if self.__shield == 1:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+4):
					obj_grid.set_grid(i,j,self.__design_shield[i-self._r][j-self._c])					

	def get_coins(self):
		return self.__coins

	def get_lives(self):
		return self.__lives

	def get_shield(self):
		return self.__shield

	def get_row(self):
		return self._r

	def get_column(self):
		return self._c

	def change_column(self,n):
		self._c += n

	def change_row(self,n):
		self._r += n					

	def toggle_shield(self):
		if self.__shield == 1:
			self.__shield = 0
		elif self.__shield == 0:
			self.__shield = 1													

	def check_coin_collision(self,obj_grid):
		if self.__shield == 0:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+3):
					if obj_grid.get_grid(i,j) == '$':
						self.__coins = self.__coins + 1

		if self.__shield == 1:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+4):
					if obj_grid.get_grid(i,j) == '$':
						self.__coins = self.__coins + 1	

	def check_obstacle_collision(self,obj_grid,start):
		if self.__shield == 0:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+3):
					if obj_grid.get_grid(i,j) == '*':
						self.__lives = self.__lives - 1
						for ii in range(obj_grid.get_grid_rows()-1):
							for jj in range(start,141+start):
								if obj_grid.get_grid(ii,jj) == '*':
									obj_grid.set_grid(ii,jj," ")


		elif self.__shield == 1:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+4):
					if obj_grid.get_grid(i,j) == '*':
						for ii in range(8):
							for jj in range(8):
								if (i-4 + ii)> -1 and (i-4 + ii) < 31 and (j-4+jj) > -1 and (j-4+jj) < 501 :
									if obj_grid.get_grid(i-4 + ii,j-4 + jj) == '*':
										obj_grid.set_grid(i-4 + ii,j-4 + jj," ")

						self.__shield = 0																		 

																

