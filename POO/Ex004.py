'''
Crie um método falar() que exibe "Olá, meu nome é {nome}".
'''

class Pessoa:
    def __init__(self, nome = ""):
        self.nome = nome
    
    def perguntar_nome(self):
        self.nome = input("Olá, me informe o seu nome: ")
    
    def falar(self):
        print(f"Olá, me chamo {self.nome}")

pessoa = Pessoa()
pessoa.perguntar_nome()
pessoa.falar()