# Python PEP 8 Best Pratices
# CRTL + Alt + L
# python3 -tt main.py - Testa o código

import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pandas import array
from pandas import (
    read_csv,
    Series,
    DataFrame,
    HDFStore
)

# from caminho_pacote import function, Classe


variavel = 0
TOTAL = 0


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
matriz = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9]


number_one = 10


# docstring
"""
    docstring em python
"""

'''
    docstring em python
'''

class Persona:
    def __init__(self, message):
        self.inicio = message
        print(self.inicio)
    pass

    def __set_name__(self, name):
        """
        Seta o nome do persona
        :param name: o nome do persona é definido pelo usuário
        :return:  não há retorno
        """
        self.name = name
        print('Welcone ', self.name)


class JuridicPerson():
    def __init__(self, message):
        self.name = None
        self.email = None
        self.inicio = message
    pass

# Best Pratices
def print_hi_with_message(name):
    pass


# Bad Pratices
def printhiwithname(name):
    pass


# Bad Pratices
def printhiwithname(x, y, z):
    t = (x + y) / z
    pass


# Bad Pratices
def printhiwithname(nota1, nota2, divisor):
    t = (nota1 + nota2) / divisor
    pass


# Best Pratices
def media_aluno(nota1, nota2, divisor):
    t = (nota1 + nota2) / divisor
    pass


# Bad Pratices
def retornofuncaoargs(
        arg_one, arg_two,
        arg_three, arg_four,
        arg_five, arg_six):
    return (arg_one + arg_two) / (arg_three + arg_four)


# Best Pratices
def retorno_funcao_args(arg_one, arg_two,
                        arg_three, arg_four,
                        arg_five, arg_six):
    pass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
