import os
import platform


def exitt():
    os._exit(0)

def clear():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')