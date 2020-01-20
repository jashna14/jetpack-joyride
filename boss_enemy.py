from colorama import init, Fore
from grid import *
from bullet import *
from mandalorian import *
init()

import os

class boss_enemy(person):
	def __init__(self,r,c):
		person.__init__(self,r,c)
		self.__design = [[' ', '/', '-', '-', '\\', ' '],['{', '(', 'O', 'O', ')', '}'],[' ', '~', '}', '{', '~', ' '],]
		self.__lives = 5
		self.__bullets = []


	def initial_placement(self,obj_grid): 
		rows = obj_grid.get_grid_rows()
		columns = obj_grid.get_grid_columns()
		for i in range(self._r,self._r+3):
			for j in range(self._c,self._c + 6):
				obj_grid.set_grid(i,j,self.__design[i- self._r][j - self._c])	

	def disappear_boss_enemy(self,obj_grid):
		for i in range(self._r,self._r+3):
			for j in range(self._c,self._c+6):
				obj_grid.set_grid(i,j," ")
			

	def reappear_boss_enemy(self,obj_grid):
		for i in range(self._r,self._r+3):
			for j in range(self._c,self._c+6):
				obj_grid.set_grid(i,j,self.__design[i-self._r][j-self._c])
	
	def move_boss_enemy(self,obj_grid,obj_mandalorian):
		if obj_mandalorian.get_row() - self._r > 5:
			self.disappear_boss_enemy(obj_grid)
			self._r += 1
			self.reappear_boss_enemy(obj_grid)
		
		elif obj_mandalorian.get_row() - self._r < -5:
			self.disappear_boss_enemy(obj_grid)
			self._r -= 1
			self.reappear_boss_enemy(obj_grid)

		elif obj_mandalorian.get_row() == 2:
			if self._r > 2:
				self.disappear_boss_enemy(obj_grid)
				self._r -= 1
				self.reappear_boss_enemy(obj_grid)

		elif obj_mandalorian.get_row() == obj_grid.get_grid_rows()-6:
			if self._r < obj_grid.get_grid_rows()-6:
				self.disappear_boss_enemy(obj_grid)
				self._r += 1
				self.reappear_boss_enemy(obj_grid)	


	def get_lives(self):
		return self.__lives

	def dec_life(self):	
		self.__lives -= 1

	def get_row(self):
		return self._r

	def get_column(self):
		return self._c	

	def shoot(self,obj_grid):
		obj_bullet = bullet(self._r +1 , self._c - 1 , 2)

		obj_bullet.reappear_bullet(obj_grid)
		self.__bullets.append(obj_bullet)

	def move_bullets(self,obj_grid,start,screen_columns,obj_mandalorian,time):
		for i in self.__bullets:
			if i.get_bullet_column() - 2 < start:
				i.disappear_bullet(obj_grid)
				self.__bullets.remove(i)
			else:
				i.disappear_bullet(obj_grid)
				m = i.move_bullet(obj_grid,obj_mandalorian,time)
				if m != 3:
					# i.reappear_bullet(obj_grid)
					m = i.move_bullet(obj_grid,obj_mandalorian,time)
					if m != 3:
						i.reappear_bullet(obj_grid)
					else:	
						self.__bullets.remove(i)
				else:
						self.__bullets.remove(i)
						
		