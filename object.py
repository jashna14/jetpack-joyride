import os
import random
from colorama import init, Fore , Style , Back
from random import seed
from random import randint
import numpy as np
init()

class object:
	def __init__(self,r,c):
		self._r = r
		self._c = c

class coin_shelves(object):
	def __init__(self,r,c):
			object.__init__(self,r,c)

def create_coinshelves(obj_grid):
	random.seed(a=None, version=2)
	coinshelves_num = randint(20,30)
	coinshelves_arr = []
	for i in range(coinshelves_num):
		obj = coin_shelves(randint(2, obj_grid.get_grid_rows() - 5),randint(10, obj_grid.get_grid_columns() - 50))
		coinshelves_arr.append(obj)

	for i in coinshelves_arr:
		for j in range(6):
			obj_grid.set_grid(i._r,i._c + j,Fore.YELLOW + Style.BRIGHT + "$" + Fore.WHITE + Style.RESET_ALL)


class firebeam(object):
	def __init__(self,r,c):
			object.__init__(self,r,c)

def create_firebeam(obj_grid,screen_columns):
	firebeam_arr = []
	random.seed(a=None, version=2)
	window_size = screen_columns // (screen_columns//20)
	grid_columns = obj_grid.get_grid_columns()
	grid_rows  = obj_grid.get_grid_rows()
	count = 0	
	while (count+1)*window_size < grid_columns - screen_columns:
		obj = firebeam(randint(2, grid_rows - 7) , randint(count*window_size,(count+1)*window_size))
		firebeam_arr.append(obj)
		count += 1

	for i in firebeam_arr:
		type = (randint(1,1000)%3)

		if type == 0:
			for j in range(4):
				obj_grid.set_grid(i._r,i._c + j,Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL)
		elif type == 1:
			for j in range(4):
				obj_grid.set_grid(i._r + j,i._c,Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL)
		elif type == 2:
			for j in range(4):
				obj_grid.set_grid(i._r + j,i._c + j,Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL)	


class powerup(object):
	def __init__(self,r,c):
			object.__init__(self,r,c)


def create_powerup(obj_grid,screen_columns,cnt):
	powerup_arr = []
	random.seed(a=None, version=2)
	grid_columns = obj_grid.get_grid_columns()
	grid_rows  = obj_grid.get_grid_rows()
	count = 0
	i = 0
	while i < cnt:
		if 1*(i)*screen_columns < grid_columns - 2*screen_columns:
			obj = powerup(randint(2, grid_rows - 6) , randint((i*1*screen_columns), (1*(i+1)*screen_columns)))
			powerup_arr.append(obj)			
			if 	obj_grid.get_grid(obj._r,obj._c) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(obj._r,obj._c+1) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(obj._r + 1,obj._c) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(obj._r + 1,obj._c+1) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(obj._r,obj._c) != Fore.MAGENTA + Style.BRIGHT + '%' + Style.RESET_ALL and obj_grid.get_grid(obj._r,obj._c+1) != Fore.MAGENTA + Style.BRIGHT + '%' + Style.RESET_ALL and obj_grid.get_grid(obj._r + 1,obj._c) != Fore.MAGENTA + Style.BRIGHT + '%' + Style.RESET_ALL and obj_grid.get_grid(obj._r + 1,obj._c+1) != Fore.MAGENTA + Style.BRIGHT + '%' + Style.RESET_ALL:
				count +=  1
				i += 1 
			else:
				powerup_arr.remove(obj)
		else:
			break			

	for j in powerup_arr:
			obj_grid.set_grid(j._r,j._c,Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL)				
			obj_grid.set_grid(j._r,j._c + 1 , Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL)				
			obj_grid.set_grid(j._r + 1,j._c ,  Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL)				
			obj_grid.set_grid(j._r + 1,j._c + 1, Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL)


class magnet(object):
	def __init__(self,r,c):
			object.__init__(self,r,c)


def create_magnet(obj_grid,screen_columns,cnt):
	magnet_arr = []
	random.seed(a=None, version=2)
	grid_columns = obj_grid.get_grid_columns()
	grid_rows  = obj_grid.get_grid_rows()

	count = 0
	i = 1
	while i < cnt:
		if 1*(i+1)*screen_columns < grid_columns - screen_columns:
			obj = magnet(14 , randint((i*1*screen_columns), (1*(i+1)*screen_columns)))
			magnet_arr.append(obj)			
			if 	obj_grid.get_grid(obj._r,obj._c) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(obj._r,obj._c+1) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(obj._r + 1,obj._c) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(obj._r + 1,obj._c+1) != Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL and obj_grid.get_grid(obj._r,obj._c) != Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL and obj_grid.get_grid(obj._r,obj._c+1) != Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL and obj_grid.get_grid(obj._r + 1,obj._c) != Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL and obj_grid.get_grid(obj._r + 1,obj._c+1) != Fore.CYAN + Style.BRIGHT + "@" + Style.RESET_ALL:
				count +=  1
				i += 1 
			else:
				magnet_arr.remove(obj)
		else:
			break			

	for j in magnet_arr:
		obj_grid.set_grid(j._r,j._c,Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL)				
		obj_grid.set_grid(j._r,j._c + 1 , Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL)				
		obj_grid.set_grid(j._r + 1,j._c ,  Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL)				
		obj_grid.set_grid(j._r + 1,j._c + 1, Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL)

	return magnet_arr	



def check_magnet_range(screen_columns,start,obj_mandalorian,last_up,obj_grid,vir_time,magnet_arr):
	
	flag = 0
	mr = obj_mandalorian.get_row()
	mc = obj_mandalorian.get_column()
	ms = obj_mandalorian.get_shield()
	
	for i in magnet_arr:
		if mc >= start and mc < start + screen_columns - 3 and i._c >= start and i._c < start + screen_columns - 3:
			flag = 1
			pos = i
			break  


	if flag == 1:
		
		if mr+3 < pos._r:
			# obj_mandalorian.change_row(min(1,14 - mr - 3))
			obj_mandalorian.change_row(1)
			last_up += 1
			obj_mandalorian.check_coin_collision(obj_grid)
			obj_mandalorian.check_powerup_collision(obj_grid,vir_time)
			obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)
			

		elif mr > pos._r+2:
			cnt = max(-3,-1*(mr - 14 - 2))
			for k in range(-1*cnt):
				obj_mandalorian.change_row(-1)
				last_up -= 1
				obj_mandalorian.check_coin_collision(obj_grid)
				obj_mandalorian.check_powerup_collision(obj_grid,vir_time)
				obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)
			

		
		if pos._c > mc+3:
			# obj_mandalorian.change_column(min(1,pos[1] - mc - 3))
			obj_mandalorian.change_column(+1)
			obj_mandalorian.check_coin_collision(obj_grid)
			obj_mandalorian.check_powerup_collision(obj_grid,vir_time)
			obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)
	
		elif pos._c + 2 < mc:
			# obj_mandalorian.change_column(max(-1,-1*(mc - pos[1] - 2)))
			cnt = min((2,(mc - pos._c - 2)))
			for k in range(cnt):
				obj_mandalorian.change_column(-2)
				obj_mandalorian.check_coin_collision(obj_grid)
				obj_mandalorian.check_powerup_collision(obj_grid,vir_time)
				obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)

	return last_up		



				
		
				

