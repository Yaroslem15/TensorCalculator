from numpy import *
from parser_t import *
from systt import *

global mas
mas = []

def basisn():    
    clear()

    R = int(input("Задайте размерность пространства: "))
    
    b = input('Введите старый базис через пробел (по строкам в одну линию): ')
    b = parse(b)
    b1=[]
    
    b1 = matrixd(b1,b,R)
    
    
    c = input('Введите новый базис через пробел (по строкам в одну линию): ')
    c = parse(c)
    c1 = []
    
    c1 = matrixd(c1,c,R)
    
    tas = dot(linalg.inv(b1),c1)
    sas = dot(linalg.inv(c1),b1)

    clear()
    
    
    def bsn1u1d(): # Не трогать!
        mas = []
        a = input('Введите тензор через пробел (по строкам в одну линию): ')
        a = parse(a)
        mas = matrixd(mas,a,R)
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
        mas = []
        a = input('Введите тензор через пробел (по строкам в одну линию): ')
        a = parse(a)
        mas = matrixd(mas,a,R)
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
        mas = []
        a = input('Введите тензор через пробел (по строкам в одну линию): ')
        print(tas)
        print(sas)
        a = parse(a)
        mas = matrixd(mas,a,R)
        asm = []
        for i in range(R):
            for j in range(R):
                am = 0
                for k in range(R):
                    for l in range(R):
                        am += tas[l][i] * mas[k][l] * tas[k][j]
                print(f'a[{i+1}][{j+1}] = q[{k+1}][{l+1}] * tas[{l+1}][{i+1}] * tas[{k+1}][{j+1}]= {mas[k][l]}*{tas[l][i]}*{tas[k][j]}={am}')
                asm.append(am)
        
        anim()
    
        print("Тензор:")
    
        asm = drix(asm, R)
    
        for i in range(R):
            print('\n')
            for j in range(R):
                print ("{:.2f}".format(asm[j][i]), end = ' ')
    
    def bsn1u2d():
        mas = []
        a = input('Введите тензор через пробел (по строкам в одну линию): ')
        a = parse(a)
        mas = matrixt(mas,a,R)
        asm = []
        for i in range(R):
            for j in range(R):
                for k in range(R):
                    am = 0
                    for l in range(R):
                        for f in range(R):
                            for n in range(R):
                                am += mas[l][f][n] * tas[l][i] * tas[n][k] * sas[j][f]
                    print(f'a[{i+1}][{j+1}][{k+1}] = q[{l+1}][{f+1}][{n+1}] * tas[{l+1}][{i+1}] * tas[{f+1}][{j+1}] * sas[{n+1}][{k+1}] = {mas[l][f][n]}*{tas[l][i]}*{tas[n][k]}*{sas[j][f]}={am}')
                    asm.append(am) 
    
        anim()
    
        print("Тензор:")
    
        asm = trix(asm, R)
    
        for i in range(R):
            print('\n________')
            for j in range(R):
                for k in range(R):
                    print ("{:.2f}".format(asm[k][i][j]), end = ' ')
                    if (k == R-1):
                        print("|", end='')
    
    def bsn2u1d():
        mas = []
        a = input('Введите тензор через пробел (по строкам в одну линию): ')
        a = parse(a)
        mas = matrixt(mas,a,R)
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
        mas = []
        a = input('Введите тензор через пробел (по строкам в одну линию): ')
        a = parse(a)
        mas = matrixt(mas,a,R)
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
        mas = []
        a = input('Введите тензор через пробел (по строкам в одну линию): ')
        a = parse(a)
        mas = matrixt(mas,a,R)
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

