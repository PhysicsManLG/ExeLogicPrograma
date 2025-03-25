'''
Exercicio 006
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''
from math import pi


raio = float(input('me informe o raio de um círculo qualquer: '))

area = pi*(raio**2)

print(f'a área do círculo de raio {raio} é {area:.2f}')