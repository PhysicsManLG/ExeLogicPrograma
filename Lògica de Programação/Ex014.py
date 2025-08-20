'''
Verifique se um ano é bissexto
'''

ano = int(input('Informe um ano qualquer: '))

if (ano % 400 == 0):{
    print(f'o ano {ano} é bissexto')
}
elif (ano % 100 == 0):{
    print(f'o ano {ano} não é bissexto')
}
elif (ano % 4 == 0):{
    print(f'o ano {ano} é bissexto')
}
else:{
    print(f'o ano {ano} não é bissexto')
}