class Espiral:

    def __init__(self):
        self.nome = ' - '
        self.quantidade = 0
        self.preco = 0

    def getNomeDoProduto(self):
        return self.nome

    def setNomeDoProduto(self, nome: str):
        self.nome = nome

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, quantidade: int):
        self.quantidade = quantidade

    def getPreco(self):
        return self.preco

    def setPreco(self, preco: float):
        self.preco = preco
