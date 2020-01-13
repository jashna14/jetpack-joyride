from getch import _getChUnix as getChar
# from __future__ import print_function
import signal

class AlarmException(Exception):
    pass
def alarmhandler(signum, frame):
            raise AlarmException
def user_input(timeout=0.1):
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                signal.signal(signal.SIGALRM, signal.SIG_IGN)
                return None