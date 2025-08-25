'''
Determine se um número é divisível por 3 e 5 ao mesmo tempo.
'''
#variável que recebe a informação do usuário
numero = int(input("Digite um número qualquer: "))

#verifica se são divisiveis e guarda as variáveis
resto_divisao5 = numero % 5
resto_divisao3 = numero % 3

#faz a validação de acordo com a condição imposta
if resto_divisao5 == 0 and resto_divisao3 ==0:
    print("O número é divisivel por 5 e 3 ao mesmo tempo")
else:
    print("não é, ao mesmo tempo.")