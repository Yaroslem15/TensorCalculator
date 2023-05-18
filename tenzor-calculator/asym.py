from numpy import *
from parser_t import *
import os

clear()

R = int(input("Задайте размерность пространства: "))


def asym():
    a = input('Введите тензор через пробел (по строкам в одну линию): ')
    a = parse(a)

    clear()

    global mas1
    mas1 = arange(R*R)
    for i in range (R*R):
        mas1[i] = a[i]
    mas1 = mas1.reshape(R, R)

    global nasm1
    nasm1 = []

    asyIJ1()

    anim()
    clear()

    for i in range(R*R):
        if i % R == 0:
            print('\n')
        print("{:.2f}".format(nasm1[i]), end=' ')

def asym2():
    a = input('Введите тензор через пробел (по строкам в одну линию): ')
    a = parse(a)

    clear()

    global mas
    mas = arange(R**3)
    for i in range (R**3):
        mas[i] = a[i]
    mas = mas.reshape(R, R, R)

    global nasm
    nasm = []

    print("Вводите следующие значения в следущем виде: [слой] [столбец] [строка]")
    match(input("По каким индексaм нужно альтернировать (введите следующим образом без пробелов: ijk): ")):
        case ('ij'):
            asyIJ()
        case ('ik'):
            asyIK()
        case ('jk'):
            asyJK()
        case ('ijk'):
            asyIJK()

    anim()
    clear()

    nasm = trix(nasm, R)
    
    for i in range(R):
        print('\n_____')
        for j in range(R):
            print ('\n')
            for k in range(R):
                print("{:.2f}".format(nasm[i][j][k]), end=' ')
    return (nasm)

def asyIK():
    for i in range(R):
        for j in range(R):
            for k in range(R):
                nasm.append((1/2) * (mas[i][j][k] - mas[j][i][k]))

def asyJK():
    for i in range(R):
        for j in range(R):
            for k in range(R):
                nasm.append((1/2) * (mas[i][j][k] - mas[k][j][i]))

def asyIJ():
    for i in range(R):
        for j in range(R):
            for k in range(R):
                nasm.append((1/2) * (mas[i][j][k] - mas[i][k][j]))

def asyIJK():
    for i in range(R):
        for j in range(R):
            for k in range(R):
                nasm.append((1/6) * (mas[i][j][k] - mas[i][k][j] + mas[j][k][i] - mas[j][i][k] + mas[k][i][j] - mas[k][j][i]))

def asyIJ1():
    for i in range(R):
        for j in range(R):
            nasm1.append((1/2) * (mas1[i][j] - mas1[j][i]))

match (int(input("Выберете один из варианттов:\n 1 - Тензор однослойный \n 2 - Тензор многослойный \n "))):
    case 1:
        asym()
    case 2:
        asym2()

input("\nНажмите Enter...")