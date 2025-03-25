'''
Exercicio 004
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

nota_01 = float(input('informe a primeira nota do aluno: '))
nota_02 = float(input('informe a segunda nota: '))
nota_03 = float(input('informe a terceira nota: '))
nota_04 = float(input('informe a última nota = '))

media = (nota_01+nota_02+nota_03+nota_04)/4

print(f'a media das notas é: {media}')