'''Utility Functions'''
import os

def playsound(path):
    '''Function to play sounds
    (Works only on Linux based OS)
    '''
    try:
        os.system('aplay -q '+ path +' 2> /dev/null &')
        os.system('afplay  '+ path +' 2> /dev/null &')
    except:
        pass

        