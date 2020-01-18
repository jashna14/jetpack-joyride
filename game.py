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

obj_grid = grid(31,500)
obj_grid.create_roof()
obj_grid.create_floor()
obj_mandalorian = mandalorian(25,0)
obj_mandalorian.initial_placement(obj_grid)
obj_coinshelves = coin_shelves()
obj_coinshelves.create_coinshelves(obj_grid)
obj_firebeam_h = firebeam_h()
obj_firebeam_h.create_firebeam_h(obj_grid)
obj_firebeam_v = firebeam_v()
obj_firebeam_v.create_firebeam_v(obj_grid)
obj_firebeam_a = firebeam_a()
obj_firebeam_a.create_firebeam_a(obj_grid)


start = 0

def move_mandalorian():

	ch = user_input()

	if ch == 'w':
		if obj_mandalorian.get_row() - 1 > 1:
			obj_mandalorian.disappear_mandalorian(obj_grid)
			obj_mandalorian.change_row(-1)
			obj_mandalorian.check_coin_collision(obj_grid)
			obj_mandalorian.check_obstacle_collision(obj_grid,start)
			obj_mandalorian.reappear_mandalorian(obj_grid)	 	

	elif ch == 'd':
		if obj_mandalorian.get_shield() == 0:
			if obj_mandalorian.get_column() + 3 < 141+start:
				obj_mandalorian.disappear_mandalorian(obj_grid)
				obj_mandalorian.change_column(+1)
				obj_mandalorian.check_coin_collision(obj_grid)
				obj_mandalorian.check_obstacle_collision(obj_grid,start)
				obj_mandalorian.reappear_mandalorian(obj_grid)

		if obj_mandalorian.get_shield() == 1:
			if obj_mandalorian.get_column() + 4 < 141+start:
				obj_mandalorian.disappear_mandalorian(obj_grid)
				obj_mandalorian.change_column(+1)
				obj_mandalorian.check_coin_collision(obj_grid)
				obj_mandalorian.check_obstacle_collision(obj_grid,start)
				obj_mandalorian.reappear_mandalorian(obj_grid)			

	elif ch == 'a':
		if obj_mandalorian.get_column() - 2 >= start:
			obj_mandalorian.disappear_mandalorian(obj_grid)
			obj_mandalorian.change_column(-2)
			obj_mandalorian.check_coin_collision(obj_grid)
			obj_mandalorian.check_obstacle_collision(obj_grid,start)
			obj_mandalorian.reappear_mandalorian(obj_grid)

	elif ch == ' ':
		if 	obj_mandalorian.get_column() + 3 < 141 + start:
			obj_mandalorian.disappear_mandalorian(obj_grid)
			obj_mandalorian.toggle_shield()
			obj_mandalorian.check_coin_collision(obj_grid)
			obj_mandalorian.check_obstacle_collision(obj_grid,start)
			obj_mandalorian.reappear_mandalorian(obj_grid)

	elif ch == 'q':
		sys.exit(0)

	else:
		if obj_mandalorian.get_row() + 1 < 26:
			obj_mandalorian.disappear_mandalorian(obj_grid)
			obj_mandalorian.change_row(+1)
			obj_mandalorian.check_coin_collision(obj_grid)
			obj_mandalorian.check_obstacle_collision(obj_grid,start)
			obj_mandalorian.reappear_mandalorian(obj_grid)										

cur_time = lambda: int(round(time.time() * 1000))
prev_time = cur_time()

os.system('clear')
while obj_mandalorian.get_lives():
	if start !=obj_grid.get_grid_columns() - 144:
		tt = cur_time()
		if tt - prev_time > 60 :
			prev_time = tt
			start = start + 1
			obj_mandalorian.disappear_mandalorian(obj_grid)
			obj_mandalorian.change_column(+1)
			obj_mandalorian.check_coin_collision(obj_grid)
			obj_mandalorian.check_obstacle_collision(obj_grid,start)
			obj_mandalorian.reappear_mandalorian(obj_grid)
	print("\033[0;0H",end = "")
	st=""
	for i in range(obj_grid.get_grid_rows()-1):
		for j in range(start,141+start):
			st += obj_grid.get_grid(i,j)
		st+="\n"
	st = st + "coins = " + 	str(obj_mandalorian.get_coins()) + "\t" + "lives = " + str(obj_mandalorian.get_lives()) + "\n"
	print(st)
	move_mandalorian()


print("GAME OVER\n")




