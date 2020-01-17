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

obj_grid = grid(31,500)
obj_grid.create_roof(obj_grid.matrix)
obj_grid.create_floor(obj_grid.matrix)
obj_mandalorian = mandalorian(25,0)
obj_mandalorian.initial_placement(obj_grid.matrix)
obj_grid.create_coinshelves(obj_grid.matrix)
obj_grid.create_obstacles_v(obj_grid.matrix)
obj_grid.create_obstacles_h(obj_grid.matrix)
obj_grid.create_obstacles_a(obj_grid.matrix)

start = 0

def move_mandalorian():

	ch = user_input()

	if ch == 'w':
		# if obj_mandalorian.r - 3 > 1:
		# 	obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
		# 	obj_mandalorian.r = obj_mandalorian.r - 3
		# 	obj_mandalorian.reappear_mandalorian(obj_grid.matrix)

		# elif obj_mandalorian.r - 2 > 1:
		# 	obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
		# 	obj_mandalorian.r = obj_mandalorian.r - 2
		# 	obj_mandalorian.reappear_mandalorian(obj_grid.matrix)

		if obj_mandalorian.r - 1 > 1:
			obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
			obj_mandalorian.r = obj_mandalorian.r - 1
			obj_mandalorian.check_coin_collision(obj_grid.matrix)
			obj_mandalorian.check_obstacle_collision(obj_grid.matrix,start,obj_grid.rows)
			obj_mandalorian.reappear_mandalorian(obj_grid.matrix)	 	

	elif ch == 'd':
		# if obj_mandalorian.c + 5 < 141+start:
		# 	obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
		# 	obj_mandalorian.c = obj_mandalorian.c + 3
		# 	obj_mandalorian.reappear_mandalorian(obj_grid.matrix)

		# elif obj_mandalorian.c + 4 < 141+start:
		# 	obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
		# 	obj_mandalorian.c = obj_mandalorian.c + 2
		# 	obj_mandalorian.reappear_mandalorian(obj_grid.matrix)

		if obj_mandalorian.shield == 0:
			if obj_mandalorian.c + 3 < 141+start:
				obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
				obj_mandalorian.c = obj_mandalorian.c + 1
				obj_mandalorian.check_coin_collision(obj_grid.matrix)
				obj_mandalorian.check_obstacle_collision(obj_grid.matrix,start,obj_grid.rows)
				obj_mandalorian.reappear_mandalorian(obj_grid.matrix)

		if obj_mandalorian.shield == 1:
			if obj_mandalorian.c + 4 < 141+start:
				obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
				obj_mandalorian.c = obj_mandalorian.c + 1
				obj_mandalorian.check_coin_collision(obj_grid.matrix)
				obj_mandalorian.check_obstacle_collision(obj_grid.matrix,start,obj_grid.rows)
				obj_mandalorian.reappear_mandalorian(obj_grid.matrix)			

	elif ch == 'a':
		# if obj_mandalorian.c - 3 >= start:
		# 	obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
		# 	obj_mandalorian.c = obj_mandalorian.c - 3
		# 	obj_mandalorian.reappear_mandalorian(obj_grid.matrix)

		# elif obj_mandalorian.c - 2 >= start:
		# 	obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
		# 	obj_mandalorian.c = obj_mandalorian.c - 2
		# 	obj_mandalorian.reappear_mandalorian(obj_grid.matrix)

		if obj_mandalorian.c - 2 >= start:
			obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
			obj_mandalorian.c = obj_mandalorian.c - 2
			obj_mandalorian.check_coin_collision(obj_grid.matrix)
			obj_mandalorian.check_obstacle_collision(obj_grid.matrix,start,obj_grid.rows)
			obj_mandalorian.reappear_mandalorian(obj_grid.matrix)

	elif ch == ' ':
		if 	obj_mandalorian.c + 3 < 141 + start:
			obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
			obj_mandalorian.shield = 1
			obj_mandalorian.check_coin_collision(obj_grid.matrix)
			obj_mandalorian.check_obstacle_collision(obj_grid.matrix,start,obj_grid.rows)
			obj_mandalorian.reappear_mandalorian(obj_grid.matrix)

	elif ch == 'q':
		sys.exit(0)
	else:
		if obj_mandalorian.r + 1 < 26:
			obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
			obj_mandalorian.r = obj_mandalorian.r + 1
			obj_mandalorian.check_coin_collision(obj_grid.matrix)
			obj_mandalorian.check_obstacle_collision(obj_grid.matrix,start,obj_grid.rows)
			obj_mandalorian.reappear_mandalorian(obj_grid.matrix)										

cur_time = lambda: int(round(time.time() * 1000))
prev_time = cur_time()

os.system('clear')
while obj_mandalorian.lives:
	if start !=obj_grid.columns - 144:
		tt = cur_time()
		if tt - prev_time > 60 :
			prev_time = tt
			start = start + 1
			obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
			obj_mandalorian.c = obj_mandalorian.c + 1
			obj_mandalorian.check_coin_collision(obj_grid.matrix)
			obj_mandalorian.check_obstacle_collision(obj_grid.matrix,start,obj_grid.rows)
			obj_mandalorian.reappear_mandalorian(obj_grid.matrix)
	obj_mandalorian.check_obstacle_collision(obj_grid.matrix,start,obj_grid.rows)
	obj_mandalorian.check_coin_collision(obj_grid.matrix)
	print("\033[0;0H",end = "")
	st=""
	for i in range(obj_grid.rows-1):
		for j in range(start,141+start):
			st+=obj_grid.matrix[i][j]
		st+="\n"
	st = st + "coins = " + 	str(obj_mandalorian.coins) + "\t" + "lives = " + str(obj_mandalorian.lives) + "\n"
	print(st)
	move_mandalorian()


print("GAME OVER\n")




