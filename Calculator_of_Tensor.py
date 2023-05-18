import os
from parser_t import *



match(int(input("Выберете действие: \n 1 - Умножение тензоров \n 2 - Нахождение тензора в новом базисе \n 3 - Симметрирование \n 4 - Альтернирование \n q - Для выхода из программы \n"))):
    case 1:
        os.system('python3 multiply.py')
    case 2:
        os.system('python3 basis-new.py')
    case 3:
        os.system('python3 sym.py')
    case 4:
        os.system('python3 asym.py')
    case ("q"):
        os.system("clear")
        anim()
        os.system("exit")
        
os.system("python3 Calculator_of_Tensor.py")
