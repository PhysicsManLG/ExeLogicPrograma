'''
Crie um construtor alternativo que receba apenas o nome e defina a idade padrão como 18.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def pegar_informacao(cls):
        nome = input("informe seu nome: ")
        return cls(nome, 18)

p = Pessoa.pegar_informacao()
print(f"{p.nome} {p.idade}")