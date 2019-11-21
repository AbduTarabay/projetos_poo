class Movimentacao:
    data=None
    valor= 0
    conta = None
    tipo = 0 # 1 - depósito / 2 - saque

    def __init__ (self,data,valor,conta):
        self.data=data
        self.valor=valor
        self.conta=conta
        self.tipo=tipo