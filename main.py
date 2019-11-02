#importanto a classe que será utilizada para criar os objetos 
from pessoa import Pessoa
from veiculo import Veiculo

def main():
    print('meu primeiro programa orientado a objetos')

    pessoa1=Pessoa()
    print(type(pessoa1))

    pessoa1.nome = 'Abdu'
    pessoa1.idade= 20
    pessoa1.sexo= 'M'
    print(f'Nome ={pessoa1.nome}')
    print(f'Idade = {pessoa1.idade}')
    print(f'Sexo = {pessoa1.sexo}')

    print(pessoa1.imprimir())

    veiculo = Veiculo('Golf','VW','Branca','1997')
    print(veiculo)


main()