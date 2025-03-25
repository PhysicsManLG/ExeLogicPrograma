'''
Exercicio 010
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
'''

graus_celsius = float(input('está quantos graus celsius? '))

graus_farenheit = ((9*graus_celsius) + 160)/5

print(f'então significa que está {graus_farenheit:.2f}º F')