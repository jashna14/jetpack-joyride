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

def stop_all_sound():
    '''Function to stop all sounds
    (Works only on Linux based OS)
    '''
    try:
        os.system("ps ax | grep aplay | grep -v grep | awk \'{print \"kill -9 \" $1}\' | sh 2> /dev/null")
        os.system("ps ax | grep afplay | grep -v grep | awk \'{print \"kill -9 \" $1}\' | sh 2> /dev/null")
    except:
        pass
        