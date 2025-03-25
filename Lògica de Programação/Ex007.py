'''
Exercicio 007
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''

lado_quadrado = float(input('informe o valor de um dos lados de um quadrado: '))

dobro_area = 2*(lado_quadrado**2)

print(f'o dobro da area do quadrado é {dobro_area:.2f}')