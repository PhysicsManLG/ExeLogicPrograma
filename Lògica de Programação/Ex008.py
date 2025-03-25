'''
Exercicio 008
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

valor_hora = float(input('informe o valor da sua hora: '))
horas_trabalhadas = float(input('qual a quantidade de horas trabalhada no mês: '))

salario_mes = valor_hora*horas_trabalhadas

print(f'baseado nas suas respostas, este mês você terá um possível salário de R$ {salario_mes}')