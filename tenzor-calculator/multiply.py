from numpy import *

import os
from parser_t import *

clear()

# Правильно читай задание и смотри, что перемножаешь!
def mul1x1():
   
    R = int(input("Задайте размерность пространства: "))

    mas1 = []

    mas2 = []

    asm = []

    a = input('Введите первый тензор через пробел: ')
    a = parse(a)
    for i in range (R):
        mas1.append(a[i])
    print(mas1)

    a = input('Введите первый тензор через пробел: ')
    a = parse(a)
    for i in range (R):
        mas2.append(a[i])

    print(mas2)    

    for i in range(R):
        for j in range(R):
            a = (mas1[i]) * (mas2[j])
            asm.append(a)
    anim()
    os.system("clear")


    print("Тензор:")
    for i in range(R*R):
        if i%R == 0 and i != 0:
            print('\n')
        print(asm[i], end=' ')

# Когда умножаем на двухвалентный
def mul1x3():

    R = int(input("Задайте размерность пространства: "))

    mas1 = []
    a = input('Введите первый тензор через пробел: ')
    a = parse(a)
    for i in range (R):
        mas1.append(a[i])
    print(mas1)

    a = input('Введите второго тензор через пробел (по строкам в одну линию): ')
    a = parse(a)
    mas2 = arange(R*R)
    for i in range (R*R):
        mas2[i] = a[i]
    mas2 = mas2.reshape(R, R)
    print(mas2)

    asm = []

    for i in range(R):
        for j in range(R):
            for k in range(R):
                asm.append(mas1[i] * mas2[k][j])
    asm = trix(asm, R)

    anim()
    clear()

    print("Тензор:")
    for i in range(R):
        print('\n')
        for j in range(R):
            for k in range(R):
                print(asm[i][j][k], end = ' ')
                if k == 2:
                    print('|', end='')

# Когда умножаем на одновалентный
def mul3x1():
    
    R = int(input("Задайте размерность пространства: "))

    a = input('Введите первый тензор через пробел (по строкам в одну линию): ')
    a = parse(a)
    mas2 = arange(R*R)
    for i in range (R*R):
        mas2[i] = a[i]
    mas2 = mas2.reshape(R, R)
    print(mas2)

    mas1 = []
    a = input('Введите второй тензор через пробел: ')
    a = parse(a)
    for i in range (R):
        mas1.append(a[i])
    print(mas1)

    asm = []

    for i in range(R):
        for j in range(R):
            for k in range(R):
                asm.append(mas2[k][j] * mas1[i])
    asm = trix(asm, R)
    anim()
    clear()

    print("Тензор:")
    for i in range(R):
        print('\n')
        for j in range(R):
            for k in range(R):
                print(asm[i][j][k], end = ' ')
                if k == 2:
                    print('|', end='')

def mul3x3():
    R = int(input("Задайте размерность пространства: "))

    a = input('Введите первый тензор через пробел (по строкам в одну линию): ')
    a = parse(a)
    mas2 = arange(R*R)
    for i in range (R*R):
        mas2[i] = a[i]
    mas2 = mas2.reshape(R, R)
    print(mas2)

    a = input('Введите второго тензор через пробел (по строкам в одну линию): ')
    a = parse(a)
    mas1 = arange(R*R)
    for i in range (R*R):
        mas1[i] = a[i]
    mas1 = mas1.reshape(R, R)
    print(mas1)

    asm = []

    for i in range(R):
        for j in range(R):
            for k in range(R):
                for l in range(R):
                    asm.append(mas2[k][l] * mas1[i][j])
    
    asm = qrix(asm, R)
    anim()
    clear()

    print("Тензор:")
    for i in range(R):
        print('\n______')
        for j in range(R):   
            print(end ='')        
            for k in range(R):
                print(end='')
                for l in range(R):
                    print(asm[i][j][k][l], end = ' ')
                    if l == R-1:
                        print("|", end = '')
                    if (l == R-1 and k == R-1):
                        print("|", end = '')


match(int(input("Выберете действие: \n 1 - Перемножение одновалентных тензоров \n 2 - Перемножение одновалентого на двухвалентный тензоров \n 3 - Перемножение двухвалентный на одновалентный тензоров \n 4 - Перемножение двухвалентных матриц \n"))):
    case 1:
        clear()
        mul1x1()
    case 2:
        clear()
        mul1x3()
    case 3:
        clear()
        mul3x1()
    case 4:
        clear()
        mul3x3()

input("\nНажмите Enter...")