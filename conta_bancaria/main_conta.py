from conta import Conta
from pessoa import Pessoa

def main():
    cliente  = Pessoa ('Edson',34,'999.999.999-99')
    #Para conseguir utilizar os valores e os métodos da conta, primeiramente é necessário instancia-la
    nova_conta=Conta()
    nova_conta.agencia =12
    nova_conta.numero =100
    nova_conta.cliente = cliente
    print('Uma nova conta for criada ')


    nova_conta.depositar(2000)

    nova_conta.depositar(500)

    nova_conta.sacar(500)

    print(f'Novo saldo: {nova_conta.saldo}')

    print(f'Agência: {nova_conta.agencia}')
    print(f'Número: {nova_conta.numero}')
    print(f'Cliente: {nova_conta.cliente.nome}')


main()