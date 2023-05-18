import time
from numpy import *

def parse(string):
    numbers = []
    current_number = ''
    for char in string:
        if char.isdigit() or char == '-':
            current_number += char
        elif current_number:
            numbers.append(float(current_number))
            current_number = ''
    if current_number:
        numbers.append(float(current_number))
    return numbers

def anim():
    for i in range(1, 101):
        print(f"Loading: {i}%", end="\r")
        time.sleep(0.01)

def drix(mass, R):
    
    new_arr = [[0 for k in range(R)] for j in range(R)]

    index = 0
    for i in range(R):
        for j in range(R):
            new_arr[i][j] = mass[index]
            index += 1
    return new_arr

def trix(mass, R):
    
    three_dim_array = [[[0 for k in range(R)] for j in range(R)] for i in range(R)]

    index = 0
    for i in range(R):
        for j in range(R):
            for k in range(R):
                three_dim_array[i][j][k] = mass[index]
                index += 1
    return three_dim_array

def qrix(mass, R):
    new_arr =  [[[[0 for l in range(R)] for k in range(R)] for j in range(R)] for i in range(R)]
    
    index = 0
    for i in range(R):
        for j in range(R):
            for k in range(R):
                for l in range(R):
                    new_arr[i][j][k][l] = mass[index]
                    index += 1
    return(new_arr)

def matrixd(mas, a, R):
    mas = arange(R*R)
    for i in range (R*R):
        mas[i] = a[i]
    mas = mas.reshape(R, R)
    return (mas)

def matrixt(mas, a, R):
    mas = arange(R**3)
    for i in range (R**3):
        mas[i] = a[i]
    mas = mas.reshape(R, R, R)
    return (mas)

import os
import platform

def clear():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')