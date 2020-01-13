import os
import random
from colorama import init, Fore
import numpy as np
init()

class grid:

	def __init__(self,rows, columns):
		self.rows = rows
		self.columns = columns
		self.matrix = np.empty([self.rows,self.columns] ,dtype='str')
		self.matrix[:] = ' '
		self.coinshelves = np.array([[10,40],[20,80],[15,95],[25,120],[22,135],[17,150],[11,170],[25,185],[17,200]])
		# self.beamver = np.array([[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,]])
		# self.beamhor = np.array([[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,]])
		# self.beamtilt = np.array([[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,],[,]])

	def create_roof(self, grid):
		for i in range(300):
			grid[0][i] = '^'
			grid[1][i] = '-' 

	def create_floor(self, grid):
		for i in range(300):
			grid[28][i] = '_'
			grid[29][i] = '^' 		

	def create_coinshelves(self,grid,coin_matrix):
		for i in range(9):
			for j in range(8):
				grid[coin_matrix[i][0]][coin_matrix[i][1]+j] = '$'


