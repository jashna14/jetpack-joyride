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
			self.__matrix[self.__rows - 3][i] = '_'
			self.__matrix[self.__rows - 2][i] = '^' 				
		 	


