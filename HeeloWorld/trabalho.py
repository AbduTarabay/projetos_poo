import os
print("\n")
print("Informe 1 para realizar um saque")
print("Informe 2 para realizar um deposito")
print("Informe 3 para retornar o extrato da conta")
print("informe 4 para sair do programa")
escolha = int(input("Qual operação você deseja realizar? "))
dinheiro = 0
while escolha != 4:
	if escolha == 1:
		valorsaque = float(input("Informe a quantidade desejada para o saque: "))
		if valorsaque <= dinheiro:
			dinheiro = dinheiro - valorsaque
			print(f"Foi sacado R$ {valordaque} da sua conta")
			arquivo = open('extrato.txt', 'r')
			conteudo = arquivo.readlines()
			conteudo.append(f'Foi realizado saque de {valorsaque}\n')
			arquivo = open('extrato.txt', 'w')
			arquivo.writelines(conteudo)
			escolha = int(input("Qual operação você deseja realizar? "))
		else:
			print("Dinheiro insuficiente na sua conta para realizar este saque")
			escolha = int(input("Qual operação você deseja realizar? "))
	elif escolha == 2:
		valordeposito = float(input("Informe a quantidade que deseja depositar: "))
		dinheiro = dinheiro + valordeposito
		print(f"Foi depositado {valordeposito} na sua conta")
		arquivo = open('extrato.txt', 'a+')
		# conteudo = arquivo.readlines()
		# conteudo.append(f'Foi realizado um deposito de {valordeposito}\n')
		# arquivo = open('extrato.txt', 'w+')
		arquivo.write(f'Foi realizado um deposito de {valordeposito}\n')
		arquivo.close()
		escolha = int(input("Qual operação você deseja realizar? "))

	elif escolha == 3:
		arquivo = open('extrato.txt', 'r')
		extrato = arquivo.read()
		arquivo.close()
		print(extrato)
		print("Saldo: %.4f"%dinheiro)
		escolha = int(input("Qual operação você deseja realizar? "))
	elif escolha == 4:
		arquivo = open('extrato.txt', 'w')
		arquivo.close()
