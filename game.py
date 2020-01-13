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

obj_grid = grid(30,300)
obj_grid.create_roof(obj_grid.matrix)
obj_grid.create_floor(obj_grid.matrix)
obj_mandalorian = mandalorian(25,0)
obj_mandalorian.initial_placement(obj_grid.matrix)
obj_grid.create_coinshelves(obj_grid.matrix,obj_grid.coinshelves)

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

		if obj_mandalorian.c + 3 < 141+start:
			obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
			obj_mandalorian.c = obj_mandalorian.c + 1
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

		if obj_mandalorian.c - 1 >= start:
			obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
			obj_mandalorian.c = obj_mandalorian.c - 1
			obj_mandalorian.reappear_mandalorian(obj_grid.matrix)

	else:
		if obj_mandalorian.r + 2 < 26:
			obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
			obj_mandalorian.r = obj_mandalorian.r + 2
			obj_mandalorian.reappear_mandalorian(obj_grid.matrix)										

cur_time = lambda: int(round(time.time() * 1000))
prev_time = cur_time()

os.system('clear')
while start != 150:
	if cur_time() - prev_time > 60 :
		start = start + 1
		obj_mandalorian.disappear_mandalorian(obj_grid.matrix)
		obj_mandalorian.c = obj_mandalorian.c + 1
		obj_mandalorian.reappear_mandalorian(obj_grid.matrix)
	# time.sleep(.1)
	print("\033[0;0f",end = "")
	# print("\033[1A",end="")
	st=""
	for i in range(obj_grid.rows):
		for j in range(start,141+start):
			# print(obj_grid.matrix[i][j],end="")
		# print()			
			st+=obj_grid.matrix[i][j]
		st+="\n"
	print(st)
	move_mandalorian()





