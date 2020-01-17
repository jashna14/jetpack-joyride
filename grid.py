import os
import random
from colorama import init, Fore
from random import seed
from random import randint
import numpy as np
init()

class grid:

	def __init__(self,rows, columns):
		self.rows = rows
		self.columns = columns
		self.matrix = np.empty([self.rows,self.columns] ,dtype='str')
		self.matrix[:] = ' '
		self.coinshelves = []
		self.obstacle_h = []
		self.obstacle_v = []
		self.obstacle_a = []

	def create_roof(self, grid):
		for i in range(self.columns):
			grid[0][i] = '^'
			grid[1][i] = '-' 

	def create_floor(self, grid):
		for i in range(self.columns):
			grid[28][i] = '_'
			grid[29][i] = '^' 		


	def create_coinshelves(self,grid):
		random.seed(a=None, version=2)
		coinshelves_num = randint(20,30)
		for _ in range(coinshelves_num):
			self.coinshelves.append([randint(2, 27),randint(10, 450)])

		for i in range(coinshelves_num):
			for j in range(6):
				grid[self.coinshelves[i][0]][self.coinshelves[i][1] + j] = '$'			

	def create_obstacles_v(self,grid):
		random.seed(a=None, version=2)
		obs_vnum = randint(7,12)
		for _ in range(obs_vnum):
			self.obstacle_v.append([randint(3, 24),randint(10, 450)])

		for i in range(obs_vnum):
			for j in range(4):
				grid[self.obstacle_v[i][0] + j][self.obstacle_v[i][1]] = '*'	

	def create_obstacles_h(self,grid):
		random.seed(a=None, version=2)
		obs_hnum = randint(7,12)
		for _ in range(obs_hnum):
			self.obstacle_h.append([randint(2, 27),randint(10, 450)])

		for i in range(obs_hnum):
			for j in range(4):
				grid[self.obstacle_h[i][0]][self.obstacle_h[i][1] + j] = '*'			

	def create_obstacles_a(self,grid):
		random.seed(a=None, version=2)
		obs_anum = randint(7,12)
		for _ in range(obs_anum):
			self.obstacle_a.append([randint(3, 24),randint(10, 450)])

		for i in range(obs_anum):
			for j in range(4):
				grid[self.obstacle_a[i][0] + j][self.obstacle_a[i][1] + j] = '*'			 	


