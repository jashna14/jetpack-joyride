from colorama import init, Fore
from grid import *
from bullet import *
init()

import os

class person:
	def __init__(self,r,c):
		self._r = r
		self._c = c
		self._design = [["|","O","|"],[" ","|"," "],["|"," ","|"]]


	def initial_placement(self,obj_grid): 
		rows = obj_grid.get_grid_rows()
		for i in range(self._r,self._r+3):
			for j in range(self._c,self._c + 3):
				obj_grid.set_grid(i,j,self._design[i- self._r][j - self._c])	

class mandalorian(person):
	def __init__(self,r,c):
		person.__init__(self,r,c)
		# self.__design = [["|","O","|"],[" ","|"," "],["|"," ","|"]]
		self.__design_jet = [["|","O","|"],[" ","|"," "],["M"," ","M"]]
		self.__design_shield = [["|","O","|","#"],[" ","|"," ","#"],["|"," ","|","#"]]
		self.__design_shield_jet = [["|","O","|","#"],[" ","|"," ","#"],["M"," ","M","#"]]
		self.__max_lives = 5
		self.__lives = 5
		self.__coins = 0
		self.__shield = 0
		self.__shield_start_time = 0
		self.__shield_end_time = 0
		self.__shield_available = 1
		self.__shield_max_time = 20
		self.__shield_max_wait_time = 40
		self.__powerup = 0
		self.__powerup_start_time = 0
		self.__powerup_max_time = 20
		self.__bullets = []



	
	# def initial_placement(self,obj_grid): 
	# 	rows = obj_grid.get_grid_rows()
	# 	for i in range(self._r,self._r+3):
	# 		for j in range(self._c,self._c + 3):
	# 			obj_grid.set_grid(i,j,self.__design[i- self._r][j - self._c])

	def disappear_mandalorian(self,obj_grid):
		if self.__shield == 0:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+3):
					obj_grid.set_grid(i,j," ")
		
		elif self.__shield == 1:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+4):
					obj_grid.set_grid(i,j," ")			

	def reappear_mandalorian(self,obj_grid,jet):
		if self.__shield == 0 and jet == 1:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+3):
					obj_grid.set_grid(i,j,self.__design_jet[i-self._r][j-self._c])

		if self.__shield == 0 and jet == 0:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+3):
					obj_grid.set_grid(i,j,self._design[i-self._r][j-self._c])
		
		if self.__shield == 1 and jet == 1:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+4):
					obj_grid.set_grid(i,j,self.__design_shield_jet[i-self._r][j-self._c])						
		
		if self.__shield == 1 and jet == 0:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+4):
					obj_grid.set_grid(i,j,self.__design_shield[i-self._r][j-self._c])					

	def get_coins(self):
		return self.__coins

	def get_lives(self):
		return self.__lives

	def get_max_lives(self):
		return self.__max_lives	

	def get_shield(self):
		return self.__shield

	def unset_shield(self,time):
		self.__shield = 0
		self.__shield_end_time = time


	def get_row(self):
		return self._r

	def get_column(self):
		return self._c

	def dec_life(self):	
		self.__lives -= 1	

	def change_column(self,n):
		self._c += n

	def change_row(self,n):
		self._r += n					

	def activate_shield(self,time):
		if self.__shield_available == 1:
			self.__shield = 1
			self.__shield_available = 0
			self.__shield_start_time = time


	def check_shield(self,time,obj_grid):
		if self.__shield == 1 and (self.__shield_start_time - time) > self.__shield_max_time:
			self.__shield = 0
			for i in range(3):
				obj_grid.set_grid(self._r + i,self._c+3,' ')
			self.__shield_end_time = time

		if self.__shield == 0 and (self.__shield_end_time - time)  > self.__shield_max_wait_time:
			self.__shield_available = 1

	def get_shield_availability(self):
		return self.__shield_available			


	def check_coin_collision(self,obj_grid):
		if self.__shield == 0:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+3):
					if obj_grid.get_grid(i,j) == '$':
						self.__coins = self.__coins + 1

		elif self.__shield == 1:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+4):
					if obj_grid.get_grid(i,j) == '$':
						self.__coins = self.__coins + 1	

	def check_powerup_collision(self,obj_grid,time):
		flag = 0
		if self.__shield == 0:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+3):
					if obj_grid.get_grid(i,j) == '@' and flag == 0:
						flag = 1
						self.__powerup = 1
						self.__powerup_start_time = time
						for ii in range(4):
								for jj in range(4):
									if (i-2 + ii)> -1 and (i-2 + ii) < obj_grid.get_grid_rows() + 1 and (j-2+jj) > -1 and (j-2+jj) < obj_grid.get_grid_columns():
										if obj_grid.get_grid(i-2 + ii,j-2 + jj) == '@':
											obj_grid.set_grid(i-2 + ii,j-2 + jj," ")

		elif self.__shield == 1:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+4):
					if obj_grid.get_grid(i,j) == '@' and flag == 0:
						flag = 1
						self.__powerup = 1
						self.__powerup_start_time = time
						for ii in range(4):
								for jj in range(4):
									if (i-2 + ii)> -1 and (i-2 + ii) < obj_grid.get_grid_rows() + 1 and (j-2+jj) > -1 and (j-2+jj) < obj_grid.get_grid_columns()  :
										if obj_grid.get_grid(i-2 + ii,j-2 + jj) == '@':
											obj_grid.set_grid(i-2 + ii,j-2 + jj," ")

	def check_powerup(self,time):
		if	self.__powerup_start_time - time > self.__powerup_max_time:
			self.__powerup = 0

	def get_powerup_status(self,time):
		return self.__powerup											

	def check_obstacle_collision(self,obj_grid,start,time):
		flag = 0
		if self.__shield == 0:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+3):
					if obj_grid.get_grid(i,j) == '*':
						if flag == 0:
							flag = 1
							self.__lives = self.__lives - 1
							self.__powerup = 0
							for ii in range(obj_grid.get_grid_rows()-1):
								for jj in range(j-4,50+j):
									if obj_grid.get_grid(ii,jj) == '*':
										obj_grid.set_grid(ii,jj," ")
													


		elif self.__shield == 1:
			for i in range(self._r,self._r+3):
				for j in range(self._c,self._c+4):
					if obj_grid.get_grid(i,j) == '*':
						if flag == 0: 
							flag = 1
							self.__shield_end_time = time
							for ii in range(8):
								for jj in range(8):
									if (i-4 + ii)> -1 and (i-4 + ii) < obj_grid.get_grid_rows() + 1 and (j-4+jj) > -1 and (j-4+jj) < obj_grid.get_grid_columns()  :
										if obj_grid.get_grid(i-4 + ii,j-4 + jj) == '*':
											obj_grid.set_grid(i-4 + ii,j-4 + jj," ")

							self.__shield = 0
							for i in range(3):
								obj_grid.set_grid(self._r + i,self._c+3,' ')


		flag = 0

	def shoot(self,obj_grid):
		if self.__shield == 0:
			obj_bullet = bullet(self._r + 1 , self._c + 3 , 1)

		if self.__shield == 1:
			obj_bullet = bullet(self._r + 1 , self._c + 4 , 1)

		obj_bullet.reappear_bullet(obj_grid)
		self.__bullets.append(obj_bullet)

	def move_bullets(self,obj_grid,start,screen_columns,obj_boss_enemy,time):
		for i in self.__bullets:
			if i.get_bullet_column() + 2 > start + screen_columns -1:
				i.disappear_bullet(obj_grid)
				self.__bullets.remove(i)
			else:
				i.disappear_bullet(obj_grid)
				m = i.move_bullet(obj_grid,obj_boss_enemy,time)
				if self.__powerup == 0:
					if m == 2 or m == 3:
						if m == 2:
							self.__coins += 5
						else:
							self.__coins += 100	
						self.__bullets.remove(i)
					else:	
						m = i.move_bullet(obj_grid,obj_boss_enemy,time)
						if m == 2 or m == 3:
							if m == 2:
								self.__coins += 5
							else:
								self.__coins += 100
							self.__bullets.remove(i)
						else:	
							i.reappear_bullet(obj_grid)

				else:
					if m == 2:
						self.__coins += 5
						self.__bullets.remove(i)
					else:	
						m = i.move_bullet(obj_grid,obj_boss_enemy,time)
						if m == 2:
							self.__coins += 5
							self.__bullets.remove(i)
						else:	
							m = i.move_bullet(obj_grid,obj_boss_enemy,time)
							if m == 2:
								self.__coins += 5
								self.__bullets.remove(i)
							else:	
								m = i.move_bullet(obj_grid,obj_boss_enemy,time)
								if m == 2:
									self.__coins += 5
									self.__bullets.remove(i)
								else:	
									m = i.move_bullet(obj_grid,obj_boss_enemy,time)
									if m == 2:
										self.__coins += 5
										self.__bullets.remove(i)
									else:	
										m = i.move_bullet(obj_grid,obj_boss_enemy,time)
										if m == 2:
											self.__coins += 5
											self.__bullets.remove(i)
										else:	
											i.reappear_bullet(obj_grid)



																

