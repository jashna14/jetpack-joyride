import os
import random
from colorama import init, Fore
from random import seed
from random import randint
import numpy as np
init()

class object:
	def __init__(self):
		self._position = []

class coin_shelves(object):
	def __init__(self):
			object.__init__(self)

	def create_coinshelves(self,obj_grid):
		random.seed(a=None, version=2)
		coinshelves_num = randint(20,30)
		for _ in range(coinshelves_num):
			self._position.append([randint(2, obj_grid.get_grid_rows() - 5),randint(10, obj_grid.get_grid_columns() - 50)])

		for i in range(coinshelves_num):
			for j in range(6):
				obj_grid.set_grid(self._position[i][0],self._position[i][1] + j,"$")

class firebeam(object):
	def __init__(self):
			object.__init__(self)

	def create_firebeam(self,obj_grid,screen_columns):
		random.seed(a=None, version=2)
		window_size = screen_columns // (screen_columns//20)
		grid_columns = obj_grid.get_grid_columns()
		grid_rows  = obj_grid.get_grid_rows()
		count = 0	
		while (count+1)*window_size < grid_columns - screen_columns:
			self._position.append([randint(2, grid_rows - 7) , randint(count*window_size,(count+1)*window_size),randint(1,1000)%3])
			count += 1
		

		for i in range(count):
			if self._position[i][2] == 0:
				for j in range(4):
					obj_grid.set_grid(self._position[i][0],self._position[i][1] + j,"*")
			elif self._position[i][2] == 1:
				for j in range(4):
					obj_grid.set_grid(self._position[i][0] + j,self._position[i][1],"*")
			elif self._position[i][2] == 2:
				for j in range(4):
					obj_grid.set_grid(self._position[i][0] + j,self._position[i][1] + j,"*")		


class powerup(object):
	def __init__(self):
			object.__init__(self)


	def create_powerup(self,obj_grid,screen_columns,cnt):
		random.seed(a=None, version=2)
		grid_columns = obj_grid.get_grid_columns()
		grid_rows  = obj_grid.get_grid_rows()
		count = 0
		for i in range(cnt):
			if 1*(i)*screen_columns < grid_columns - 2*screen_columns:
				self._position.append([randint(2, grid_rows - 6) , randint((i*1*screen_columns), (1*(i+1)*screen_columns))])
				if 	obj_grid.get_grid(self._position[i][0],self._position[i][1]) != '*' and obj_grid.get_grid(self._position[i][0],self._position[i][1]+1) != '*':
					count +=  1
				else:
					i -= 1	

		for i in range(count):
				obj_grid.set_grid(self._position[i][0],self._position[i][1],'@')				
				obj_grid.set_grid(self._position[i][0],self._position[i][1] + 1 , '@')				
				obj_grid.set_grid(self._position[i][0] + 1,self._position[i][1] ,  '@')				
				obj_grid.set_grid(self._position[i][0] + 1,self._position[i][1] + 1, '@')				
		
				

