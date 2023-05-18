import os
import platform
from parser_t import *

match(input("Выберете действие: \n 1 - Умножение тензоров \n 2 - Нахождение тензора в новом базисе \n 3 - Симметрирование \n 4 - Альтернирование \n q - Для выхода из программы \n")):
    case '1':
        system = platform.system()
        if system == 'Windows':
            os.system('python multiply.py')
        else:
            os.system('python3 multiply.py')
    case '2':
        system = platform.system()
        if system == 'Windows':
            os.system('python basis-new.py')
        else:
            os.system('python3 basis-new.py')
    case '3':
        system = platform.system()
        if system == 'Windows':
            os.system('python sym.py')
        else:
            os.system('python3 sym.py')
    case '4':
        system = platform.system()
        if system == 'Windows':
            os.system('python asym.py')
        else:
            os.system('python3 asym.py')
    case ("q"):
        print()

input("\nНажмите Enter...")
