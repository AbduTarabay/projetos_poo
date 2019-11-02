from conta import Conta
def main():
    #Para conseguir utilizar os valores e os métodos da conta, primeiramente é necessário instancia-la
    nova_conta=Conta()
    print('Uma nova conta for criada ')


    nova_conta.depositar(0)

    nova_conta.depositar(0)

    nova_conta.sacar()

    print(f'Novo saldo: {nova_conta.saldo}')


main()