#!/data/data/com.termux/files/usr/bin/python

# func.py

import os

# Variables globales que usaré dentro de funciones.
a = ''
b = ''
c = ''
x = ''

def intro():
    print('REGLAS DE TRES')
    print('++++++++++++++++++++++++++++++++')
    print ('Si la relación entre las magnitudes es directa (cuando aumenta una magnitud también lo hace la otra) hay que aplicar la REGLA DE TRES SIMPLE DIRECTA.\n')

    print ('Por el contrario, si la relación entre las magnitudes es inversa (cuando aumenta una magnitud disminuye la otra) se aplica la REGLA DE TTES SIMPLE INVERSA.')
    print('++++++++++++++++++++++++++++++++\n')

def datos():
    # Cuando use estas variables en la función serán las globales, no las locales.
    global a
    global b
    global c
    
    print ('Primero introducuremos los valores "a" y "b" que son los que nos van a indicar en que proporciòn debe cambiar "c" para ser "x".\n')

    a = input('Introduce el valor de "a": ')

    b = input('Introduce el valor de "b": ')

    print('\nAhora introduciremos el valor de "c" que cambiará en la misma proporciòn que "a" respecto a "b" para darnos el valor de "x".')
    c = input('\nIntroduce el valor de "c": ')

def directa(a, b, c):
    global x
    #       b * c
    #   x = -----
    #         a 
    x = (b * c) / a

    print(f'El valor de "x" es {x}.')
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    print(f' {a} ----> {b} ')
    print(f' {c} ----> {x} ')

def inversa(a, b, c):
    global x
    #       a * b
    #   x = -----
    #         c
    x = (a * b) / c

    print(f'El valor de "x" es {x}.')
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    print(f' {a} ----> {b} ')
    print(f' {c} ----> {x} ')
    print('~~~~~~~~~~~~~~~~~~~~~~~')

def menu():
    print ('¿Que regla de tres necesitas?\n')

    print ('1) SIMPLE DIRECTA.')
    print ('2) SIMPLE INVERSA.')

    select = input('>>> ')

    if int(select) == 1:
        os.system('clear')
        print('Regla de tres simple directa.\n')
        datos()
        directa(int(a),int(b), int(c))
    elif int(select) == 2:
        os.system('clear')
        print('Regla de tres simple inversa')
        datos()
        inversa(int(a),int(b), int(c))
    else:
        os.system('clear')
        print('Opciòn no reconocida, indica 1 o 2 para referirte a una de las reglas de tres.\n')
        intro()
        menu()


