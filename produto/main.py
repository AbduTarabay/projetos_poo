from produto_regra import ProdutoRegra
def mostrar_menu() :
    print('1 - Cadastrar')
    print('2 - Visualizar')
    print('0 - Sair')

    opcao= -1
    try:
        opcao = int(input('Digite uma das opções: '))
    except ValueError:
        print('Valor informado deve ser um número!')

    if opcao > 2 or opcao < 0:
        print('Opção inválida')
        return 0

    return opcao

def main():
    produto_regra = ProdutoRegra()
    
    opcao_retornada = -1
    while opcao_retornada !=0:

        opcao_retornada=mostrar_menu()

    if opcao_retornada == 1:
        print('Escolheu a opção 1')

    elif opcao_retornada == 2:
        print2('Escolheu a opção 2 ') 
    else:
        print('Escolheu a opção 0')
        

main()