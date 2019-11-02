class Conta :
    agencia = 0
    numero = 0
    saldo = 0

    def depositar(self,valor):

        self.saldo += valor
        print(f'Depósito de {valor} efetuado com sucesso!')

    def sacar (self,valor):
        if self.saldo >= valor:
            print('saldo insuficiente')
        else:
            self.saldo -= valor
            print(f'Saque de {valor} efetuadoo com sucesso!')

