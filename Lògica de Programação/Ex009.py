'''
Exercicio 009
Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
'''

garus_farenheit = float(input('me informe quantos º F está fazendo: '))

graus_celsius = (5*(garus_farenheit-32)/9)

print(f'Então significa que está fazendo {graus_celsius:.2f} º C.')