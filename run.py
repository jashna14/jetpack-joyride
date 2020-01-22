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
from utilities import *

cur_time = lambda: int(round(time.time() * 1000))

def play():

	screen_rows = 30
	screen_columns = 141
	grid_columns = 1000
	obj_grid = grid(screen_rows,grid_columns)
	obj_grid.create_roof()
	obj_grid.create_floor()
	obj_mandalorian = mandalorian(screen_rows - 6,0)
	obj_mandalorian.initial_placement(obj_grid)
	obj_boss_enemy = boss_enemy(screen_rows - 6,grid_columns-6)
	obj_boss_enemy.initial_placement(obj_grid)
	create_coinshelves(obj_grid)
	create_firebeam(obj_grid,screen_columns)
	create_powerup(obj_grid,screen_columns,8)
	magnet_arr = create_magnet(obj_grid,screen_columns,3)

	start = 0
	vir_time = 600


	def move_mandalorian(last_up):

		if screen_rows - 6 == obj_mandalorian.get_row():
			last_up = screen_rows - 6

		ch = user_input()

		if ch == 'w' or ch == 'W':
			if obj_mandalorian.get_row() - 1 > 1:
				if obj_mandalorian.get_shield() == 0:
					if obj_grid.get_grid(obj_mandalorian.get_row() - 1,obj_mandalorian.get_column()) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() - 1,obj_mandalorian.get_column() + 1) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() - 1,obj_mandalorian.get_column() + 2) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL:
						obj_mandalorian.disappear_mandalorian(obj_grid)
						last_up -= 1 
						obj_mandalorian.change_row(-1)
						obj_mandalorian.check_coin_collision(obj_grid)
						obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
						obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
						obj_mandalorian.reappear_mandalorian(obj_grid,1)

				elif obj_mandalorian.get_shield() == 1:
					if obj_grid.get_grid(obj_mandalorian.get_row() - 1,obj_mandalorian.get_column()) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() - 1,obj_mandalorian.get_column() + 1) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() - 1,obj_mandalorian.get_column() + 2) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() - 1,obj_mandalorian.get_column() + 3) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL:
						obj_mandalorian.disappear_mandalorian(obj_grid)
						last_up -= 1 
						obj_mandalorian.change_row(-1)
						obj_mandalorian.check_coin_collision(obj_grid)
						obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
						obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
						obj_mandalorian.reappear_mandalorian(obj_grid,1)				 	

		elif ch == 'd' or ch == 'D':

			if obj_mandalorian.get_shield() == 0:
				if obj_mandalorian.get_column() + 3 < screen_columns+start:
					obj_mandalorian.disappear_mandalorian(obj_grid)
					if obj_grid.get_grid(obj_mandalorian.get_row(),obj_mandalorian.get_column()+3) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 1,obj_mandalorian.get_column() + 3) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 2,obj_mandalorian.get_column() + 3) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL:
						obj_mandalorian.change_column(+1)
						obj_mandalorian.check_coin_collision(obj_grid)
						obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
						obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
					
					change = 0	
					if obj_mandalorian.get_row() + (obj_mandalorian.get_row() - last_up)//10 + 1 < screen_rows - 5:
						change = (obj_mandalorian.get_row() - last_up)//10 + 1
					elif screen_rows - 6 - obj_mandalorian.get_row() > 0:
						change = screen_rows - 6 - obj_mandalorian.get_row()
						last_up = screen_rows - 6	

					for j in range(change):
						if obj_grid.get_grid(obj_mandalorian.get_row()+3,obj_mandalorian.get_column()) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + 1) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + 2) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL :
							obj_mandalorian.change_row(+1)					
							obj_mandalorian.check_coin_collision(obj_grid)
							obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
							obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
						else:
							break	
					obj_mandalorian.reappear_mandalorian(obj_grid,0)

			elif obj_mandalorian.get_shield() == 1:
				if obj_mandalorian.get_column() + 4 < screen_columns+start:
					obj_mandalorian.disappear_mandalorian(obj_grid)
					if obj_grid.get_grid(obj_mandalorian.get_row(),obj_mandalorian.get_column()+4) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 1,obj_mandalorian.get_column() + 4) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 2,obj_mandalorian.get_column() + 4) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL:
						obj_mandalorian.change_column(+1)
						obj_mandalorian.check_coin_collision(obj_grid)
						obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
						obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
				
					change = 0	
					if obj_mandalorian.get_row() + (obj_mandalorian.get_row() - last_up)//10 + 1 < screen_rows - 5:
						change = (obj_mandalorian.get_row() - last_up)//10 + 1
					elif screen_rows - 6 - obj_mandalorian.get_row() > 0:
						change = screen_rows - 6 - obj_mandalorian.get_row()
						last_up = screen_rows - 6 	

					for j in range(change):
						if obj_grid.get_grid(obj_mandalorian.get_row()+3,obj_mandalorian.get_column()) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + 1) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + 2) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + 3) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL:
							obj_mandalorian.change_row(+1)					
							obj_mandalorian.check_coin_collision(obj_grid)
							obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
							obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
						else:
							break	
					obj_mandalorian.reappear_mandalorian(obj_grid,0)			

		elif ch == 'a'  or ch == 'S':

			obj_mandalorian.disappear_mandalorian(obj_grid)
			if obj_mandalorian.get_column() - 2 >= start:
				if obj_grid.get_grid(obj_mandalorian.get_row(),obj_mandalorian.get_column()-2) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 1,obj_mandalorian.get_column() -2) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 2,obj_mandalorian.get_column() -2) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL:
					obj_mandalorian.change_column(-2)
					obj_mandalorian.check_coin_collision(obj_grid)
					obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
					obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
			
			change = 0	
			if obj_mandalorian.get_row() + (obj_mandalorian.get_row() - last_up)//10 + 1 < screen_rows - 5:
				change = (obj_mandalorian.get_row() - last_up)//10 + 1
			elif screen_rows - 6 - obj_mandalorian.get_row() > 0:
				change = screen_rows - 6 - obj_mandalorian.get_row()
				last_up = screen_rows - 6 	

			if obj_mandalorian.get_shield() == 1:
				x = 3
			else:
				x = 0	

			for j in range(change):
				if obj_grid.get_grid(obj_mandalorian.get_row()+3,obj_mandalorian.get_column()) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + 1) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + 2) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + x) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL:
					obj_mandalorian.change_row(+1)					
					obj_mandalorian.check_coin_collision(obj_grid)
					obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
					obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
				else:
					break	
			obj_mandalorian.reappear_mandalorian(obj_grid,0)		

		elif ch == ' ':

			if 	obj_mandalorian.get_column() + 3 < screen_columns + start:
				if obj_grid.get_grid(obj_mandalorian.get_row(),obj_mandalorian.get_column()+ 3) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 1,obj_mandalorian.get_column() + 3) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 2,obj_mandalorian.get_column() + 3) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL:
					obj_mandalorian.disappear_mandalorian(obj_grid)
					obj_mandalorian.activate_shield(vir_time//1)
					obj_mandalorian.check_coin_collision(obj_grid)
					obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
					obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
					obj_mandalorian.reappear_mandalorian(obj_grid,0)
				else:	
					obj_mandalorian.disappear_mandalorian(obj_grid)
					obj_mandalorian.change_column(-1)					
					obj_mandalorian.activate_shield(vir_time//1)
					obj_mandalorian.check_coin_collision(obj_grid)
					obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
					obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
					obj_mandalorian.reappear_mandalorian(obj_grid,0)

		elif ch == 'q' or ch == 'Q':
			os.system('clear')
			print(Style.BRIGHT + Fore.RED + 'Terminating Game ...' + Style.RESET_ALL)
			for i in range(30):
				print()
			time.sleep(1.5)
			sys.exit(0)

		elif ch == 's' or ch == 'S':
			obj_mandalorian.shoot(obj_grid)
			obj_mandalorian.disappear_mandalorian(obj_grid)
			change = 0	
			if obj_mandalorian.get_row() + (obj_mandalorian.get_row() - last_up)//4 + 1 < screen_rows - 5:
				change = (obj_mandalorian.get_row() - last_up)//4 + 1
			elif screen_rows - 6 - obj_mandalorian.get_row() > 0:
				change = screen_rows - 6 - obj_mandalorian.get_row()
				last_up = screen_rows - 6

			if obj_mandalorian.get_shield() == 1:
				x = 3
			else:
				x = 0		

			for j in range(change):
				if obj_grid.get_grid(obj_mandalorian.get_row()+3,obj_mandalorian.get_column()) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + 1) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + 2) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + x) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL:
					obj_mandalorian.change_row(+1)					
					obj_mandalorian.check_coin_collision(obj_grid)
					obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
					obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
				else:
					break	
			obj_mandalorian.reappear_mandalorian(obj_grid,0)	
			


		else:

			obj_mandalorian.disappear_mandalorian(obj_grid)
			change = 0	
			if obj_mandalorian.get_row() + (obj_mandalorian.get_row() - last_up)//10 + 1 < screen_rows - 5:
				change = (obj_mandalorian.get_row() - last_up)//10 + 1
			elif screen_rows - 6 - obj_mandalorian.get_row() > 0:
				change = screen_rows - 6 - obj_mandalorian.get_row()
				last_up = screen_rows - 6 	

			if obj_mandalorian.get_shield() == 1:
				x = 3
			else:
				x = 0	

			for j in range(change):
				if obj_grid.get_grid(obj_mandalorian.get_row()+3,obj_mandalorian.get_column()) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + 1) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + 2) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 3,obj_mandalorian.get_column() + x) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL:
					obj_mandalorian.change_row(+1)					
					obj_mandalorian.check_coin_collision(obj_grid)
					obj_mandalorian.check_powerup_collision(obj_grid,vir_time//1)
					obj_mandalorian.check_obstacle_collision(obj_grid,start,vir_time//1)
				else:
					break	
			obj_mandalorian.reappear_mandalorian(obj_grid,0)
		return last_up								

	prev_time = cur_time()
	prev_time1 = cur_time()
	prev_time3 = cur_time()
	flag  = 0
	last_up = 0
	
	os.system('clear')
	while obj_mandalorian.get_lives() > 0 and (vir_time//1 > 0) and obj_boss_enemy.get_lives() > 0:
		if cur_time() - prev_time1 > 90:
			vir_time -= 0.5
			prev_time1 = cur_time()
			obj_mandalorian.check_shield(vir_time,obj_grid)
			obj_mandalorian.check_powerup(vir_time)

		if cur_time() - prev_time3 > 100:
			obj_mandalorian.disappear_mandalorian(obj_grid)
			last_up = check_magnet_range(screen_columns,start,obj_mandalorian,last_up,obj_grid,vir_time//1,magnet_arr)
			obj_mandalorian.reappear_mandalorian(obj_grid,0)
			prev_time3 = cur_time()


		if start == obj_grid.get_grid_columns() - screen_columns and flag == 0:
			prev_time2 =  vir_time//1
			flag = 1	

		if start !=obj_grid.get_grid_columns() - screen_columns:
			tt = cur_time()
			if tt - prev_time > 60 :
				prev_time = tt
				change = 0
				if obj_mandalorian.get_powerup_status(vir_time//1):
					if start + 3 < obj_grid.get_grid_columns() - screen_columns + 1:
						change = 3

					elif start + 2 < obj_grid.get_grid_columns() - screen_columns + 1:
						change = 2

					elif start + 1 < obj_grid.get_grid_columns() - screen_columns + 1:
						change = 1												
				else:
					change = 1

				obj_mandalorian.disappear_mandalorian(obj_grid)
				for k in range(change):
					if obj_mandalorian.get_shield == 0:
						x = 0
					else:
						x = 1 	
					if obj_grid.get_grid(obj_mandalorian.get_row(),obj_mandalorian.get_column()+ 3 + x) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 1,obj_mandalorian.get_column() + 3+x) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL and obj_grid.get_grid(obj_mandalorian.get_row() + 2,obj_mandalorian.get_column() + 3 + x) != Fore.MAGENTA + Style.BRIGHT + "%" + Style.RESET_ALL:
						start = start + 1	
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
		print(st1,end = "\r")
		last_up = move_mandalorian(last_up)
		obj_boss_enemy.move_boss_enemy(obj_grid,obj_mandalorian)


	os.system('clear')
	if obj_mandalorian.get_lives() <= 0:	
		with open('resources/youlose_ascii.txt') as f:
			while True:
				c = f.read(1)
				if not c:
					break
				else:	
					print(Fore.RED + Style.BRIGHT + c + Style.RESET_ALL,end = "")
		for i in range(25):
			print()
						
	elif obj_boss_enemy.get_lives() <= 0:
		while(obj_mandalorian.get_column() != obj_grid.get_grid_columns() - 4):
			obj_boss_enemy.disappear_boss_enemy(obj_grid)
			if cur_time() - prev_time1 > 20:
				prev_time1 = cur_time()
				obj_mandalorian.disappear_mandalorian(obj_grid)
				obj_mandalorian.change_column(+1)
				obj_mandalorian.reappear_mandalorian(obj_grid,0)
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
				print(st1,end = "\r")


		with open('resources/youwin_ascii.txt') as f:
			while True:
				c = f.read(1)
				if not c:
					break
				else:	
					print(Fore.RED + Style.BRIGHT + c + Style.RESET_ALL,end = "")

		for i in range(25):
			print()			
	else:
		with open('resources/youlose_ascii.txt') as f:
			while True:
				c = f.read(1)
				if not c:
					break
				else:	
					print(Fore.RED + Style.BRIGHT + c + Style.RESET_ALL,end = "")	

		for i in range(25):
			print()
	
os.system('clear')
# playsound('resources/itsame.wav')
ti = cur_time()

matrix = []

row = 0
column = 0
with open("resources/save_master_yoda_ascii.txt") as fileobj:
	for line in fileobj:  
		matrix.append(line.split('c'))

matrix2 = []

row = 0
column = 0
with open("resources/yoda_ascii.txt") as fileobj:
	for line in fileobj:  
		matrix2.append(line.split('\n'))
	
	
matrix3 = [[" " for i in range(141)]for j in range(30)]

for i in range(17):
	for j in range(74):
		matrix3[i][j] = matrix[i][0][j]

for i in range(20):
	for j in range(74,119):
		matrix3[i][j] = matrix2[i][0][j - 74]

st = ''
for i in range(30):
	for j in range(141):
		st+= Style.BRIGHT + Fore.CYAN + matrix3[i][j] + Style.RESET_ALL
	st+='\n'



print(st)

while(cur_time() -ti < 3000):	
	continue

# print("\033[0K",end = "")
os.system('clear')
print(Style.BRIGHT + Fore.MAGENTA + 'INSTRUCTIONS' + Style.RESET_ALL)
print(
    '>> : Press ' +
    Style.BRIGHT +
    Fore.CYAN +
    'w' +
    Style.RESET_ALL +
    ' to move UP')
print(
    '>> : Press ' +
    Style.BRIGHT +
    Fore.CYAN +
    'd' +
    Style.RESET_ALL +
    ' to move RIGHT')
print(
    '>> : Press ' +
    Style.BRIGHT +
    Fore.CYAN +
    'a' +
    Style.RESET_ALL +
    ' to move LEFT')
print(
    '>> : Press ' +
    Style.BRIGHT +
    Fore.CYAN +
    's' +
    Style.RESET_ALL +
    ' to SHOOT')
print(
    '>> : Press ' +
    Style.BRIGHT +
    Fore.CYAN +
    'SPACEBAR' +
    Style.RESET_ALL +
    ' to Activate SHIELD')
print(
    '>> : Press ' +
    Style.BRIGHT +
    Fore.CYAN +
    'q' +
    Style.RESET_ALL +
    ' to Exit')

print('\nPress P to Play\n')
choice = input('OPTION : ')
if choice ==  'p' or choice ==  'P':
	print("\033[0;0H",end = "")
	play()

elif choice == 'q' or choice == 'Q':
	os.system('clear')
	print(Style.BRIGHT + Fore.RED + 'Terminating Game ...' + Style.RESET_ALL)
	for i in range(30):
		print()
	time.sleep(1.5)
	sys.exit(0)	
else:
    os.system('clear')
    print(Style.BRIGHT + Fore.RED + 'INVALID OPTION' + Style.RESET_ALL)
    print('Terminating Game ...')
    for i in range(30):
    	print()
    time.sleep(1.5)
    sys.exit(0)








