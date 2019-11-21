from produto import Produto

class ProdutoRegra:

def cadastrar (self):
    print('\n===========CADASTRO PRODUTO===========')

    nome= input('Informe o nome : ')
    marca = input('Informe a marca : ')
    quantidade = float(input('Informe a quantidade : '))
    valor= float(input('Informe o valor: '))

    produto_novo = Produto (nome,marca,quantidade,valor)