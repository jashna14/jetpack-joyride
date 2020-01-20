import os
import random
from colorama import init, Fore
from random import seed
from random import randint
import numpy as np
init()

class bullet:

	def __init__(self,row,column,person):
		self.__r = row
		self.__c = column
		self.__previous = ' '
		self.__person = person
		if person == 1:
			self.__design = 'o'
		elif person == 2:
			self.__design = '<'	

	def reappear_bullet(self,obj_grid):
		current_char = obj_grid.get_grid(self.__r,self.__c)
		if current_char == '$' or current_char == '@':
			self.__previous = current_char
		else:
			self.__previous = ' '

		obj_grid.set_grid(self.__r,self.__c,self.__design)

	def disappear_bullet(self,obj_grid):
		obj_grid.set_grid(self.__r,self.__c,self.__previous)		

	def move_bullet(self,obj_grid,obj_person,time):
		if self.__person == 1:
			self.__c += 1
			if self.__c < obj_grid.get_grid_columns():
				if obj_grid.get_grid(self.__r,self.__c) == '*':
					i = self.__r
					j = self.__c
					for ii in range(8):
						for jj in range(8):
							if (i-4 + ii)> -1 and (i-4 + ii) < obj_grid.get_grid_rows() + 1 and (j-4+jj) > -1 and (j-4+jj) < obj_grid.get_grid_columns():
								if obj_grid.get_grid(i-4 + ii,j-4 + jj) == '*':
									obj_grid.set_grid(i-4 + ii,j-4 + jj," ")
					return 2

				elif self.__r >= obj_person.get_row() and self.__r < obj_person.get_row()+3 and self.__c >= obj_person.get_column() and self.__c < obj_person.get_column()+3:
					obj_person.dec_life()
					return 3							

		elif self.__person == 2:
			self.__c -= 1
			if obj_person.get_shield() == 0:
				if self.__r >= obj_person.get_row() and self.__r < obj_person.get_row()+3 and self.__c >= obj_person.get_column() and self.__c < obj_person.get_column()+3:
					obj_person.dec_life()
					return 3

			if obj_person.get_shield() == 1:
				if self.__r >= obj_person.get_row() and self.__r < obj_person.get_row()+3 and self.__c >= obj_person.get_column() and self.__c < obj_person.get_column()+4:
					# obj_person.dec_life()
					obj_person.unset_shield(time)
					# obj_person.__shield_end_time = time + 90
					for i in range(3):
						obj_grid.set_grid(obj_person.get_row() + i,obj_person.get_column() + 3,' ')
					return 3		


	def get_bullet_column(self):	
		return self.__c
