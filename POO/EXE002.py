class Produto:
    def __init__(self, nome, preco):
        self.nome=nome
        self.preco=preco
    
    def desconto(self, percento):
        self.preco=self.preco-(self.preco*(percento/100))

    #getter(sempre que pedir, vai passar por aqui primeiro)
    @property
    def preco(self):
        return self._preco

    #setter (vai passar por aqui para configurar)
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
            
        self._preco = valor

produto1 = Produto('livro', 165)
produto1.desconto(10)
print(produto1.preco)

produto2 = Produto('manga', 'R$35')
produto2.desconto(10)
print(produto2.preco)