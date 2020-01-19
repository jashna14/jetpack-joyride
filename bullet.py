import os
import random
from colorama import init, Fore
from random import seed
from random import randint
import numpy as np
init()

class bullet:

	def __init__(self,row,column):
		self.__r = row
		self.__c = column
