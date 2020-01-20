import signal
import os
import time
import sys
import tty
import termios
import numpy as np
from colorama import init, Fore , Style , Back
init()

from grid import *
from mandalorian import *
from input import *
from object import *
from boss_enemy import *

cur_time = lambda: int(round(time.time() * 1000))

def play():

	screen_rows = 30
	screen_columns = 141
	grid_columns = 500
	obj_grid = grid(screen_rows,grid_columns)
	obj_grid.create_roof()
	obj_grid.create_floor()
	obj_mandalorian = mandalorian(screen_rows - 6,0)
	obj_mandalorian.initial_placement(obj_grid)
	obj_boss_enemy = boss_enemy(screen_rows - 6,grid_columns-6)
	obj_boss_enemy.initial_placement(obj_grid)
	obj_coinshelves = coin_shelves()
	obj_coinshelves.create_coinshelves(obj_grid)
	obj_firebeam = firebeam()
	obj_firebeam.create_firebeam(obj_grid,screen_columns)
	obj_powerup = powerup()
	obj_powerup.create_powerup(obj_grid,screen_columns,8)

	start = 0
	vir_time = 300
	last_up_time = 0


	def move_mandalorian():

		ch = user_input()

		if ch == 'w':
			if obj_mandalorian.get_row() - 1 > 1:
				last_up_time = 0
				obj_mandalorian.disappear_mandalorian(obj_grid)
				obj_mandalorian.change_row(-1)
				obj_mandalorian.check_coin_collision(obj_grid)
				obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
				obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
				obj_mandalorian.reappear_mandalorian(obj_grid,1)	 	

		elif ch == 'd':
			if obj_mandalorian.get_shield() == 0:
				if obj_mandalorian.get_column() + 3 < screen_columns+start:
					obj_mandalorian.disappear_mandalorian(obj_grid)
					obj_mandalorian.change_column(+1)
					obj_mandalorian.check_coin_collision(obj_grid)
					obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
					obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
					obj_mandalorian.reappear_mandalorian(obj_grid,0)

			if obj_mandalorian.get_shield() == 1:
				if obj_mandalorian.get_column() + 4 < screen_columns+start:
					obj_mandalorian.disappear_mandalorian(obj_grid)
					obj_mandalorian.change_column(+1)
					obj_mandalorian.check_coin_collision(obj_grid)
					obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
					obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
					obj_mandalorian.reappear_mandalorian(obj_grid,0)			

		elif ch == 'a':
			if obj_mandalorian.get_column() - 2 >= start:
				obj_mandalorian.disappear_mandalorian(obj_grid)
				obj_mandalorian.change_column(-2)
				obj_mandalorian.check_coin_collision(obj_grid)
				obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
				obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
				obj_mandalorian.reappear_mandalorian(obj_grid,0)

		elif ch == ' ':
			if 	obj_mandalorian.get_column() + 3 < screen_columns + start:
				obj_mandalorian.disappear_mandalorian(obj_grid)
				obj_mandalorian.activate_shield(vir_time//1)
				obj_mandalorian.check_coin_collision(obj_grid)
				obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
				obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
				obj_mandalorian.reappear_mandalorian(obj_grid,0)

		elif ch == 'q':
			sys.exit(0)

		elif ch == 's':
			obj_mandalorian.shoot(obj_grid)	

		else:
			if obj_mandalorian.get_row() + 1 < screen_rows - 5:
				obj_mandalorian.disappear_mandalorian(obj_grid)
				obj_mandalorian.change_row(+1)
				obj_mandalorian.check_coin_collision(obj_grid)
				obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
				obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
				obj_mandalorian.reappear_mandalorian(obj_grid,0)										

	prev_time = cur_time()
	prev_time1 = cur_time()
	flag  = 0
	
	os.system('clear')
	
	while obj_mandalorian.get_lives() and (vir_time//1 > 0) and obj_boss_enemy.get_lives():
		if cur_time() - prev_time1 > 90:
			vir_time -= 0.5
			prev_time1 = cur_time()
			obj_mandalorian.check_shield(vir_time,obj_grid)
			obj_mandalorian.check_powerup(vir_time)

		if start == obj_grid.get_grid_columns() - screen_columns and flag == 0:
			prev_time2 =  vir_time//1
			flag = 1	

		if start !=obj_grid.get_grid_columns() - screen_columns:
			tt = cur_time()
			if tt - prev_time > 60 :
				prev_time = tt
				if obj_mandalorian.get_powerup_status(vir_time//1):
					if start + 3 < obj_grid.get_grid_columns() - screen_columns + 1:
						start = start + 3
						obj_mandalorian.disappear_mandalorian(obj_grid)
						obj_mandalorian.change_column(+3)
					elif start + 2 < obj_grid.get_grid_columns() - screen_columns + 1:
						start = start + 2
						obj_mandalorian.disappear_mandalorian(obj_grid)
						obj_mandalorian.change_column(+2)

					elif start + 1 < obj_grid.get_grid_columns() - screen_columns + 1:
						start = start + 1
						obj_mandalorian.disappear_mandalorian(obj_grid)
						obj_mandalorian.change_column(+1)												
				else:
					start = start + 1 	
					obj_mandalorian.disappear_mandalorian(obj_grid)
					obj_mandalorian.change_column(+1)
					
				obj_mandalorian.check_coin_collision(obj_grid)
				obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
				obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
				obj_mandalorian.move_bullets(obj_grid,start,screen_columns,obj_boss_enemy,vir_time//1)
				obj_mandalorian.reappear_mandalorian(obj_grid,0)

		else:
			tt = cur_time()
			if tt - prev_time > 60 :
				prev_time = tt
				obj_mandalorian.move_bullets(obj_grid,start,screen_columns,obj_boss_enemy,vir_time//1)
				obj_boss_enemy.move_bullets(obj_grid,start,screen_columns,obj_mandalorian,vir_time//1)

			if prev_time2 - vir_time//1  > 3: 	
				prev_time2 = vir_time//1	
				obj_boss_enemy.shoot(obj_grid)

		print("\033[0;0H",end = "")
		st=""
		for i in range(obj_grid.get_grid_rows()):
			for j in range(start,screen_columns+start):
				st += obj_grid.get_grid(i,j)
			st+="\n"
		print(st)	
		print("\033[0K",end = "")
		st1 = ""	
		st1 = st1 + "💵 :" + 	str(obj_mandalorian.get_coins()) + "  " + "lives = " 
		for i in range(obj_mandalorian.get_lives()):
			st1 = st1 + '❤️  '
		for i in range(obj_mandalorian.get_max_lives() - obj_mandalorian.get_lives()):
			st1 = st1 + '   '	
		st1 = st1 + " " + "enemy_lives = "
		for i in range(obj_boss_enemy.get_lives()):
			st1 = st1 + '❤️  '
		for i in range(obj_boss_enemy.get_max_lives() - obj_boss_enemy.get_lives()):
			st1 = st1 + '   '	 
		st1 = st1 +  "  " + "time remaining = " + str(vir_time//1) + "  " + "shield = " + str(obj_mandalorian.get_shield_availability()) + "\n"
		print(st1)
		move_mandalorian()
		obj_boss_enemy.move_boss_enemy(obj_grid,obj_mandalorian)


	print("GAME OVER\n")			

	
# def Start_game():
os.system('clear')
# playsound('resources/itsame.wav')
ti = cur_time()
print(Style.BRIGHT + Fore.CYAN + 'WELCOME TO JETPACK-JOYRIDE' + Style.RESET_ALL,end = "\r")
while(cur_time() -ti < 300):	
	continue

print("\033[0K",end = "")
print(Style.BRIGHT + Fore.MAGENTA + 'INSTRUCTIONS' + Style.RESET_ALL)
print(
    'Level 0 : Conventional Mario with ' +
    Style.BRIGHT +
    Fore.CYAN +
    'No' +
    Style.RESET_ALL +
    ' Enemies')
print(
    'Level 1 : Conventional Mario with ' +
    Style.BRIGHT +
    Fore.GREEN +
    'Easy' +
    Style.RESET_ALL +
    ' Enemies')
print(
    'Level 2 : Conventional Mario with ' +
    Style.BRIGHT +
    Fore.YELLOW +
    'Difficult' +
    Style.RESET_ALL +
    ' Enemies')
print('Level 3 : Conventional Mario with ' + Style.BRIGHT +
      Fore.RED + 'Impossible' + Style.RESET_ALL + ' Enemies')
print('\nPress p to Play\n')
choice = input('OPTION : ')
if choice is 'p':
	start = 0
	vir_time = 300
	last_up_time = 0
	print("\033[0;0H",end = "")
	play()
try:
    choice = int(choice)
except ValueError:
    print("\033[0;0H",end = "")
    print(Style.BRIGHT + Fore.RED + 'INVALID OPTION' + Style.RESET_ALL)
    print('Terminating Game ...')
    # time.sleep(1.5)
    sys.exit(0)







