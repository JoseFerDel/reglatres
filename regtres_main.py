#!/data/data/com.termux/files/usr/bin/python

# regtres_main.py

import os

import func

# ++++++++++++++++++++++++++++
# a ----> b
# c ----> x
# (a es a b lo que c es a x)
# ++++++++++++++++++++++++++++
# Regla de tres simple directa.
#     b * c
# x = -----
#       a
# +++++++++++++++++++++++++++++
# Regla de tres simple inversa.
#     a * b
# x = -----
#       c
# ++++++++++++++++++++++++++++

os.system('clear')


func.intro()

func.menu()
