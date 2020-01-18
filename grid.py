import os
import random
from colorama import init, Fore
from random import seed
from random import randint
import numpy as np
init()

class grid:

	def __init__(self,rows, columns):
		self.__rows = rows
		self.__columns = columns
		self.__matrix = np.empty([self.__rows,self.__columns] ,dtype='str')
		self.__matrix[:] = ' '
		self.__coinshelves = []
		self.__obstacle_h = []
		self.__obstacle_v = []
		self.__obstacle_a = []

	def set_grid(self,r,c,x):
		self.__matrix[r][c] = x

	def get_grid(self,r,c):
		return self.__matrix[r][c]

	def get_grid_rows(self):
		return self.__rows

	def get_grid_columns(self):
		return self.__columns				

	def create_roof(self):
		for i in range(self.__columns):
			self.__matrix[0][i] = '^'
			self.__matrix[1][i] = '-' 

	def create_floor(self):
		for i in range(self.__columns):
			self.__matrix[28][i] = '_'
			self.__matrix[29][i] = '^' 		


	def create_coinshelves(self):
		random.seed(a=None, version=2)
		coinshelves_num = randint(20,30)
		for _ in range(coinshelves_num):
			self.__coinshelves.append([randint(2, 27),randint(10, 450)])

		for i in range(coinshelves_num):
			for j in range(6):
				self.__matrix[self.__coinshelves[i][0]][self.__coinshelves[i][1] + j] = '$'			

	def create_obstacles_v(self):
		random.seed(a=None, version=2)
		obs_vnum = randint(7,12)
		for _ in range(obs_vnum):
			self.__obstacle_v.append([randint(3, 24),randint(10, 450)])

		for i in range(obs_vnum):
			for j in range(4):
				self.__matrix[self.__obstacle_v[i][0] + j][self.__obstacle_v[i][1]] = '*'	

	def create_obstacles_h(self):
		random.seed(a=None, version=2)
		obs_hnum = randint(7,12)
		for _ in range(obs_hnum):
			self.__obstacle_h.append([randint(2, 27),randint(10, 450)])

		for i in range(obs_hnum):
			for j in range(4):
				self.__matrix[self.__obstacle_h[i][0]][self.__obstacle_h[i][1] + j] = '*'			

	def create_obstacles_a(self):
		random.seed(a=None, version=2)
		obs_anum = randint(7,12)
		for _ in range(obs_anum):
			self.__obstacle_a.append([randint(3, 24),randint(10, 450)])

		for i in range(obs_anum):
			for j in range(4):
				self.__matrix[self.__obstacle_a[i][0] + j][self.__obstacle_a[i][1] + j] = '*'			 	


