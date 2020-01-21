import os
import random
from colorama import init, Fore , Style , Back
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
				obj_grid.set_grid(self._position[i][0],self._position[i][1] + j,Fore.YELLOW + Style.BRIGHT + "$" + Fore.WHITE + Style.RESET_ALL)

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
					obj_grid.set_grid(self._position[i][0],self._position[i][1] + j,Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL)
			elif self._position[i][2] == 1:
				for j in range(4):
					obj_grid.set_grid(self._position[i][0] + j,self._position[i][1],Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL)
			elif self._position[i][2] == 2:
				for j in range(4):
					obj_grid.set_grid(self._position[i][0] + j,self._position[i][1] + j,Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL)		


class powerup(object):
	def __init__(self):
			object.__init__(self)


	def create_powerup(self,obj_grid,screen_columns,cnt):
		random.seed(a=None, version=2)
		grid_columns = obj_grid.get_grid_columns()
		grid_rows  = obj_grid.get_grid_rows()
		count = 0
		i = 0
		while i < cnt:
			if 1*(i)*screen_columns < grid_columns - 2*screen_columns:
				self._position.append([randint(2, grid_rows - 6) , randint((i*1*screen_columns), (1*(i+1)*screen_columns))])
				# print(self._position)
				# print(i)			
				if 	obj_grid.get_grid(self._position[i][0],self._position[i][1]) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(self._position[i][0],self._position[i][1]+1) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(self._position[i][0] + 1,self._position[i][1]+1) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(self._position[i][0] + 1,self._position[i][1]+1) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(self._position[i][0],self._position[i][1]) != Fore.MAGENTA + Style.BRIGHT + '%' + Style.RESET_ALL and obj_grid.get_grid(self._position[i][0],self._position[i][1]+1) != Fore.MAGENTA + Style.BRIGHT + '%' + Style.RESET_ALL and obj_grid.get_grid(self._position[i][0] + 1,self._position[i][1]+1) != Fore.MAGENTA + Style.BRIGHT + '%' + Style.RESET_ALL and obj_grid.get_grid(self._position[i][0] + 1,self._position[i][1]+1) != Fore.MAGENTA + Style.BRIGHT + '%' + Style.RESET_ALL:
					count +=  1
					i += 1 
				else:
					self._position.remove(self._position[i])
			else:
				break			

		for j in range(count):
				obj_grid.set_grid(self._position[j][0],self._position[j][1],Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL)				
				obj_grid.set_grid(self._position[j][0],self._position[j][1] + 1 , Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL)				
				obj_grid.set_grid(self._position[j][0] + 1,self._position[j][1] ,  Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL)				
				obj_grid.set_grid(self._position[j][0] + 1,self._position[j][1] + 1, Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL)



class magnet(object):
	def __init__(self):
			object.__init__(self)


	def create_magnet(self,obj_grid,screen_columns,cnt):
		random.seed(a=None, version=2)
		grid_columns = obj_grid.get_grid_columns()
		grid_rows  = obj_grid.get_grid_rows()

		count = 0
		i = 1
		while i < cnt:
			if 1*(i+1)*screen_columns < grid_columns - screen_columns:
				self._position.append([14 , randint((i*1*screen_columns), (1*(i+1)*screen_columns))])
				# print(self._position)
				# print(i)			
				if 	obj_grid.get_grid(self._position[i-1][0],self._position[i-1][1]) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(self._position[i-1][0],self._position[i-1][1]+1) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(self._position[i-1][0] + 1,self._position[i-1][1]+1) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(self._position[i-1][0] + 1,self._position[i-1][1]+1) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(self._position[i-1][0],self._position[i-1][1]) != Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL and obj_grid.get_grid(self._position[i-1][0],self._position[i-1][1]+1) != Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL and obj_grid.get_grid(self._position[i-1][0] + 1,self._position[i-1][1]+1) != Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL and obj_grid.get_grid(self._position[i-1][0] + 1,self._position[i-1][1]+1) != Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL:
					count +=  1
					i += 1 
				else:
					self._position.remove(self._position[i-1])
			else:
				break			

		for j in range(count):
				obj_grid.set_grid(self._position[j][0],self._position[j][1],Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL)				
				obj_grid.set_grid(self._position[j][0],self._position[j][1] + 1 , Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL)				
				obj_grid.set_grid(self._position[j][0] + 1,self._position[j][1] ,  Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL)				
				obj_grid.set_grid(self._position[j][0] + 1,self._position[j][1] + 1, Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL)

	
	def check_magnet_range(self,screen_columns,start,obj_mandalorian,last_up,obj_grid,vir_time):
		
		flag = 0
		mr = obj_mandalorian.get_row()
		mc = obj_mandalorian.get_column()
		ms = obj_mandalorian.get_shield()
		
		for i in self._position:
			if mc >= start and mc < start + screen_columns - 3 and i[1] >= start and i[1] < start + screen_columns - 3:
				flag = 1
				pos = i
				break  


		if flag == 1:
			
			if mr+3 < 14:
				# obj_mandalorian.change_row(min(1,14 - mr - 3))
				obj_mandalorian.change_row(1)
				last_up += 1
				obj_mandalorian.check_coin_collision(obj_grid)
				obj_mandalorian.check_powerup_collision(obj_grid,vir_time)
				obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)
				

			elif mr > 14+2:
				cnt = max(-3,-1*(mr - 14 - 2))
				for k in range(-1*cnt):
					obj_mandalorian.change_row(-1)
					last_up -= 1
					obj_mandalorian.check_coin_collision(obj_grid)
					obj_mandalorian.check_powerup_collision(obj_grid,vir_time)
					obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)
				

			
			if pos[1] > mc+3:
				# obj_mandalorian.change_column(min(1,pos[1] - mc - 3))
				obj_mandalorian.change_column(+1)
				obj_mandalorian.check_coin_collision(obj_grid)
				obj_mandalorian.check_powerup_collision(obj_grid,vir_time)
				obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)
		
			elif pos[1] + 2 < mc:
				# obj_mandalorian.change_column(max(-1,-1*(mc - pos[1] - 2)))
				for k in range(3):
					obj_mandalorian.change_column(-1)
					obj_mandalorian.check_coin_collision(obj_grid)
					obj_mandalorian.check_powerup_collision(obj_grid,vir_time)
					obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)

		return last_up		



				
		
				

