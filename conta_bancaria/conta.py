from movimentacao import Movimentacao
import datetime
class Conta :
    agencia = 0
    numero = 0
    saldo = 0
    cliente=None
    movimentacoes = []

    def depositar(self,valor):

        self.saldo += valor
        #Para cada depósito gera um novo objeto movimentação
        #com os dados da movimentação
        mov_deposito = Movimentacao(datetime.datetime.now(),valor,self)
        #Após gerar o novo movimento, ele é armazenado no atributo movimentacoes
        self.movimentacoes.append(mov_deposito)
        print(f'Depósito de {valor} efetuado com sucesso!')

    def sacar (self,valor):
        if (self.saldo >= valor):
            self.saldo-=valor
            mov_saque=Movimentacao(datetime.datetime.now(),valor,self)
            print('saldo insuficiente')
        else:
            self.saldo -= valor
            print(f'Saque de {valor} efetuadoo com sucesso!')

