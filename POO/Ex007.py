'''
Utilize propriedades (@property) para acessar idade e email.
'''

class Pessoa():
    def __init__(self, nome="", idade=0, email=""):
        self.nome = nome
        self._idade = idade
        self._email = email
    
    def pegar_informacao(self):
        self.nome = input("informe nome: ")
        self._idade = int(input("informe idade: "))
        self._email = input("informe email: ")

    @property
    def idade(self):
        return self._idade
    
    @property
    def email(self):
        return self._email
    

pessoa = Pessoa()
pessoa.pegar_informacao()
print(pessoa.nome)
print(pessoa.idade)
print(pessoa.email)