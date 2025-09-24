'''
Adicione um método estático que retorna a quantidade total de objetos Pessoa criados.
'''

class Pessoa:
    total_pessoas = 0

    def __init__(self, nome=""):
        self.nome=nome
        self.lista = []
        Pessoa.total_pessoas += 1

    def adicionar_nome_lista(self, valor):
        self.lista.append(valor)
    
    def contar_nomes_lista(self):
        return len(self.lista)
    
    def mostrar_nomes_lista(self):
        for i, lista in enumerate(self.lista, start=1):
            print(f"{i}: {lista}")
    
    @staticmethod
    def quantidade_total():
        return Pessoa.total_pessoas
    

minha_lista = Pessoa()

minha_lista.adicionar_nome_lista(input("Informe um nome: "))
minha_lista.adicionar_nome_lista(input("Informe outro nome: "))

print(f"a liste tem {minha_lista.contar_nomes_lista()} nomes.")

minha_lista.mostrar_nomes_lista()