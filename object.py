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
			self._position.append([randint(2, obj_grid.get_grid_rows() - 4),randint(10, obj_grid.get_grid_columns() - 50)])

		for i in range(coinshelves_num):
			for j in range(6):
				obj_grid.set_grid(self._position[i][0],self._position[i][1] + j,"$")

class firebeam_h(object):
	def __init__(self):
			object.__init__(self)

	def create_firebeam_h(self,obj_grid):
		random.seed(a=None, version=2)
		obs_hnum = randint(7,12)
		for _ in range(obs_hnum):
			self._position.append([randint(2, obj_grid.get_grid_rows() - 4),randint(10, obj_grid.get_grid_columns() - 50)])

		for i in range(obs_hnum):
			for j in range(4):
				obj_grid.set_grid(self._position[i][0],self._position[i][1] + j,"*")


class firebeam_v(object):
	def __init__(self):
			object.__init__(self)

	def create_firebeam_v(self,obj_grid):
		random.seed(a=None, version=2)
		obs_vnum = randint(7,12)
		for _ in range(obs_vnum):
			self._position.append([randint(2, obj_grid.get_grid_rows() - 4),randint(10, obj_grid.get_grid_columns() - 50)])

		for i in range(obs_vnum):
			for j in range(4):
				obj_grid.set_grid(self._position[i][0] + j,self._position[i][1],"*")


class firebeam_a(object):
	def __init__(self):
			object.__init__(self)

	def create_firebeam_a(self,obj_grid):
		random.seed(a=None, version=2)
		obs_anum = randint(7,12)
		for _ in range(obs_anum):
			self._position.append([randint(2, obj_grid.get_grid_rows() - 4),randint(10, obj_grid.get_grid_columns() - 50)])

		for i in range(obs_anum):
			for j in range(4):
				obj_grid.set_grid(self._position[i][0] + j,self._position[i][1] + j,"*")									
