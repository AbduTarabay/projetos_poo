class Produto:
    nome = ''
    marca = ''
    quantidade = 0
    valor = 0

    #Método construtor
    def __init__(self,nome,marca,quantidade,valor):
        self.nome = nome
        self.marca = marca
        self.quantidade = quantidade
        self.valor = valor