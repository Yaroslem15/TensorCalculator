import asym
import basis
import multiply_t
import sym

from parser_t import *
from systt import *

while(True):
    clear()
    match(input("Выберете действие: \n 1 - Умножение тензоров \n 2 - Нахождение тензора в новом базисе \n 3 - Симметрирование \n 4 - Альтернирование \n q - Для выхода из программы \n")):
        case '1':
            multiply_t.multiplis()
        case '2':
            basis.basisn()
        case '3':
            sym.symming()
        case '4':
            asym.asymming()
        case ("q"):
            exitt()
    input("\nНажмите Enter...")