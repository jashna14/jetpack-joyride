import signal
import os
import time
import sys
import tty
import termios
import numpy as np
from colorama import init, Fore
init()

from grid import *
from mandalorian import *
from input import *
from object import *

screen_rows = 30
screen_columns = 141
obj_grid = grid(screen_rows,1000)
obj_grid.create_roof()
obj_grid.create_floor()
obj_mandalorian = mandalorian(screen_rows - 6,0)
obj_mandalorian.initial_placement(obj_grid)
obj_coinshelves = coin_shelves()
obj_coinshelves.create_coinshelves(obj_grid)
obj_firebeam = firebeam()
obj_firebeam.create_firebeam(obj_grid,screen_columns)


start = 0
vir_time = 0

def move_mandalorian():

	ch = user_input()

	if ch == 'w':
		if obj_mandalorian.get_row() - 1 > 1:
			obj_mandalorian.disappear_mandalorian(obj_grid)
			obj_mandalorian.change_row(-1)
			obj_mandalorian.check_coin_collision(obj_grid)
			obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)
			obj_mandalorian.reappear_mandalorian(obj_grid)	 	

	elif ch == 'd':
		if obj_mandalorian.get_shield() == 0:
			if obj_mandalorian.get_column() + 3 < screen_columns+start:
				obj_mandalorian.disappear_mandalorian(obj_grid)
				obj_mandalorian.change_column(+1)
				obj_mandalorian.check_coin_collision(obj_grid)
				obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)
				obj_mandalorian.reappear_mandalorian(obj_grid)

		if obj_mandalorian.get_shield() == 1:
			if obj_mandalorian.get_column() + 4 < screen_columns+start:
				obj_mandalorian.disappear_mandalorian(obj_grid)
				obj_mandalorian.change_column(+1)
				obj_mandalorian.check_coin_collision(obj_grid)
				obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)
				obj_mandalorian.reappear_mandalorian(obj_grid)			

	elif ch == 'a':
		if obj_mandalorian.get_column() - 2 >= start:
			obj_mandalorian.disappear_mandalorian(obj_grid)
			obj_mandalorian.change_column(-2)
			obj_mandalorian.check_coin_collision(obj_grid)
			obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)
			obj_mandalorian.reappear_mandalorian(obj_grid)

	elif ch == ' ':
		if 	obj_mandalorian.get_column() + 3 < screen_columns + start:
			obj_mandalorian.disappear_mandalorian(obj_grid)
			obj_mandalorian.activate_shield(vir_time)
			obj_mandalorian.check_coin_collision(obj_grid)
			obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)
			obj_mandalorian.reappear_mandalorian(obj_grid)

	elif ch == 'q':
		sys.exit(0)

	else:
		if obj_mandalorian.get_row() + 1 < screen_rows - 5:
			obj_mandalorian.disappear_mandalorian(obj_grid)
			obj_mandalorian.change_row(+1)
			obj_mandalorian.check_coin_collision(obj_grid)
			obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)
			obj_mandalorian.reappear_mandalorian(obj_grid)										

cur_time = lambda: int(round(time.time() * 1000))
prev_time = cur_time()

os.system('clear')
while obj_mandalorian.get_lives():
	if start !=obj_grid.get_grid_columns() - screen_columns - 3:
		tt = cur_time()
		if tt - prev_time > 60 :
			vir_time += 0.5
			obj_mandalorian.check_shield(vir_time//1)
			prev_time = tt
			start = start + 1
			obj_mandalorian.disappear_mandalorian(obj_grid)
			obj_mandalorian.change_column(+1)
			obj_mandalorian.check_coin_collision(obj_grid)
			obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time)
			obj_mandalorian.reappear_mandalorian(obj_grid)
	print("\033[0;0H",end = "")
	st=""
	for i in range(obj_grid.get_grid_rows()-1):
		for j in range(start,screen_columns+start):
			st += obj_grid.get_grid(i,j)
		st+="\n"
	st = st + "coins = " + 	str(obj_mandalorian.get_coins()) + "  " + "lives = " + str(obj_mandalorian.get_lives()) +  "  " + "time = " + str(vir_time//1) + "  " + "shield = " + str(obj_mandalorian.get_shield_availability()) + "\n"
	print(st)
	move_mandalorian()


print("GAME OVER\n")




