'''
Determine se um número digitado é positivo, negativo ou zero.
'''

numero = float(input("Digite um número qualquer: "))

if numero > 0:{
    print(f'o número {numero} é positivo')
    }
elif numero < 0:{
    print(f'o número {numero} é negtivo')
    }
else:{
    print(f'o numero {numero} é igual a 0')
}