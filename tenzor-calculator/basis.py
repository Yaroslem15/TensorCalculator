from numpy import *
from parser_t import *
from systt import *

def basisn():    
    clear()
    
    R = int(input("Задайте размерность пространства: "))
    
    mas = []
    
    b = input('Введите старый базис через пробел (по строкам в одну линию): ')
    b = parse(b)
    b1=[]
    
    b1 = matrixd(b1,b,R)
    
    
    c = input('Введите новый базис через пробел (по строкам в одну линию): ')
    c = parse(c)
    c1 = []
    
    c1 = matrixd(c1,c,R)
    
    try:
        tas = dot(linalg.inv(b1),c1)
        sas = dot(linalg.inv(c1),b1)
    except ValueError:
        print("Ошибка: некорректное значение, повторите попытку!")
        clear()
        basisn()
        
    
    def layer1():
        global mas
        mas = []
        a = input('Введите тензор через пробел (по строкам в одну линию): ')
        a = parse(a)
        mas = matrixd(mas,a,R)
    
    def layer2():
        global mas
        mas = []
        a = input('Введите тензор через пробел (по строкам в одну линию): ')
        a = parse(a)
        mas = matrixt(mas,a,R)
    
    
    
    def bsn1u1d(): # Не трогать!
        asm = []
        for i in range(R):
            for j in range(R):
                for k in range(R):
                    for l in range(R):
                        asm.append(tas[l][i] * mas[k][l] * sas[j][k]); 
        
        anim()
        clear()
    
        print("Тензор:")
        asm = drix(asm, R)
        for i in range(R):
            print('\n')
            for j in range(R):
                print ("{:.2f}".format(asm[j][i]), end = ' ')
    
    def bsn2u():
        asm = []
        for i in range(R):
            for j in range(R):
                am = 0
                for k in range(R):
                    for l in range(R):
                        am += sas[i][l] * mas[k][l] * sas[j][k]
                asm.append(am); 
    
        anim()
        clear()
    
        print("Тензор:")
    
        asm = drix(asm, R)
        for i in range(R):
            print('\n')
            for j in range(R):
                print ("{:.2f}".format(asm[j][i]), end = ' ')
    
    def bsn2d(): # Не трогать!
        asm = []
        for i in range(R):
            for j in range(R):
                am = 0
                for k in range(R):
                    for l in range(R):
                        am += tas[l][i] * mas[k][l] * tas[k][j]
                asm.append(am)
        
        anim()
        clear()
    
        print("Тензор:")
    
        asm = drix(asm, R)
    
        for i in range(R):
            print('\n')
            for j in range(R):
                print ("{:.2f}".format(asm[j][i]), end = ' ')
    
    def bsn1u2d():
        asm = []
        for i in range(R):
            for j in range(R):
                for k in range(R):
                    am = 0
                    for l in range(R):
                        for f in range(R):
                            for n in range(R):
                                am += tas[n][i] * mas[l][f][n] * tas[f][j] * sas[k][l]
                    asm.append(am) 
    
        anim()
        clear()
    
        print("Тензор:")
    
        asm = trix(asm, R)
    
        for i in range(R):
            print('\n')
            for j in range(R):
                for k in range(R):
                    print ("{:.2f}".format(asm[k][i][j]), end = ' ')
                    if (j == 0) and (k != 0):
                        print("||", end='')
    
    def bsn2u1d():
        asm = []
        for i in range(R):
            for j in range(R):
                for k in range(R):
                    am = 0
                    for l in range(R):
                        for f in range(R):
                            for n in range(R):
                                am += tas[n][i] * mas[l][f][n] * sas[j][f] * sas[k][l]
                    asm.append(am); 
    
        anim()
        clear()
    
        print("Тензор:")
    
        asm = trix(asm, R)
    
        for i in range(R):
            print('\n')
            for j in range(R):
                for k in range(R):
                    print ("{:.2f}".format(asm[k][i][j]), end = ' ')
                    if (j == 0) and (k != 0):
                        print("||", end='')
    
    def bsn3u(): # не трогать!
        asm = []
        for i in range(R):
            for j in range(R):
                for k in range(R):
                    am = 0
                    for l in range(R):
                        for f in range(R):
                            for n in range(R):
                                am += sas[k][l] * mas[l][f][n] * sas[j][f] * sas[i][n]
                    asm.append(am)
    
        anim()
        clear()
    
        print("Тензор:")
    
        asm = trix(asm, R)
    
        for i in range(R):
            print('\n')
            for j in range(R):
                for k in range(R):
                    print ("{:.2f}".format(asm[k][i][j]), end = ' ')
                    if (j == 0) and (k != 0):
                        print("||", end='')
        
    
    def bsn3d():
        asm = []
        for i in range(R):
            for j in range(R):
                for k in range(R):
                    am = 0
                    for l in range(R):
                        for f in range(R):
                            for n in range(R):
                                am +=tas[l][k] * mas[l][f][n] * tas[f][j] * tas[n][i]
                    asm.append(am); 
    
        anim()
        clear()
    
        print("Тензор:")
    
        asm = trix(asm, R)
    
        for i in range(R):
            print('\n')
            for j in range(R):
                for k in range(R):
                    print ("{:.2f}".format(asm[k][i][j]), end = ' ')
                    if (j == 0) and (k != 0):
                        print("||", end='')
        
    
    clear()
    match(int(input("Выберете один из варианттов:\n 1 - Тензор однослойный \n 2 - Тензор многослойный \n "))):
        case(1):
            clear()
            layer1()
        case(2):
            clear()
            layer2()
    
    clear()
    match(input("Введите количество верхних и нижних регистров следующим образом без пробела (если есть только верхние или нижние, второе число запишите как 0): [верхний][нижний] \n")):
        case('11'):
            bsn1u1d()
        case('20'):
            bsn2u()
        case('02'):
            bsn2d()
        case('12'):
            bsn1u2d()
        case('21'):
            bsn2u1d()
        case('30'):
            bsn3u()
        case('03'):
            bsn3d()

