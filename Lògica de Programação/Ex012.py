'''
Verifique se um número é par ou ímpar.
'''

numero = float(input('Olá.\nDigite um número qualquer: '))

resto = numero % 2

if resto == 0:{
    print(f'O número {numero} é par')
}
else:{
    print(f'o número é ímpar!')
}