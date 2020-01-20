import os
import random
from colorama import init, Fore , Style, Back
from random import seed
from random import randint
import numpy as np
init()

class grid:

	def __init__(self,rows, columns):
		self.__rows = rows
		self.__columns = columns
		self.__matrix = [[" " for i in range(self.__columns)]for j in range(self.__rows)]
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
			if i % 2 == 0:
				self.__matrix[0][i] = Fore.RED + Style.BRIGHT + '(' + Style.RESET_ALL
			elif i % 2 == 1:
				self.__matrix[0][i] = Fore.RED + Style.BRIGHT + ')' + Style.RESET_ALL

		for i in range(self.__columns):
			self.__matrix[1][i] = Fore.RED + Style.BRIGHT + '-' + Style.RESET_ALL			


	def create_floor(self):
		for i in range(self.__columns):
			if i % 3 == 0:
				self.__matrix[self.__rows - 3][i] = Fore.YELLOW + Style.BRIGHT + '_' + Style.RESET_ALL
			elif i % 3 == 1:
				self.__matrix[self.__rows - 3][i] = Fore.YELLOW + Style.BRIGHT + '_' + Style.RESET_ALL
			elif i % 3 == 2:
				self.__matrix[self.__rows - 3][i] = Fore.YELLOW + Style.BRIGHT + '_' + Style.RESET_ALL		

		for i in range(self.__columns):
			if i % 3 == 0:
				self.__matrix[self.__rows - 2][i] = Fore.RED + Style.BRIGHT + '_' + Style.RESET_ALL
			elif i % 3 == 1:
				self.__matrix[self.__rows - 2][i] = Fore.RED + Style.BRIGHT + '_' + Style.RESET_ALL
			elif i % 3 == 2:
				self.__matrix[self.__rows - 2][i] = Fore.RED + Style.BRIGHT + '|' + Style.RESET_ALL

		for i in range(self.__columns):
			if i % 3 == 0:
				self.__matrix[self.__rows - 1][i] = Fore.RED + Style.BRIGHT + '_' + Style.RESET_ALL
			elif i % 3 == 1:
				self.__matrix[self.__rows - 1][i] = Fore.RED + Style.BRIGHT + '|' + Style.RESET_ALL
			elif i % 3 == 2:
				self.__matrix[self.__rows - 1][i] = Fore.RED + Style.BRIGHT + '_' + Style.RESET_ALL							
		 	


