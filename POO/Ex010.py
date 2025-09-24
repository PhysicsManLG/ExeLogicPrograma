'''
Modifique a classe para incluir um atributo de classe total_pessoas que conte quantos objetos foram instanciados.
'''

class Pessoa:
    total_pessoas = 0

    def __init__(self, nome=""):
        self.nome=nome
        Pessoa.total_pessoas += 1
   
    @staticmethod
    def quantidade_total():
        return Pessoa.total_pessoas
    
pessoa1 = Pessoa('Guts')
pessoa2 = Pessoa('Casca')
pessoa3 = Pessoa('Griffith')

print(f"{Pessoa.quantidade_total()} pessoas")