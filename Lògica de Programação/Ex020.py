'''
Verifique se uma palavra é um palíndromo
'''

palavra = input("informe uma palavra qualquer: ")
palavra = palavra.replace(" ","").lower()

if palavra == palavra[::-1]:
    print(" é um palíndromo")
else:
    print("não é um palíndromo")