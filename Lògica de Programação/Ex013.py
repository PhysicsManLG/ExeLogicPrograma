'''
Peça três números e exiba o maior.
'''

numero1= int(input('olá.\nInforme um numero, inteiro, qualquer: '))
numero2= int(input('Informe um outro numero, inteiro, qualquer: '))
numero3= int(input('Informe o último numero, inteiro, qualquer: '))

if numero1 > numero2 and numero1 > numero3:{
    print(f'o primeiro número escolhido, {numero1}, é maior que {numero2} e {numero3}')
}
elif numero2 > numero3 and numero2 > numero1:{
    print(f'o segundo numero escolhido, {numero2}, é maior que {numero1} e {numero3}')
}
elif numero3 > numero1 and numero3 > numero2:{
    print(f'o terceiro numero escolhido, {numero3}, é maior que {numero1} e {numero2}')
}
else:{
    print('os números são iguais')
}