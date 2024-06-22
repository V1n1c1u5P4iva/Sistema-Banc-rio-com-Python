menu = """
    Escolha a opção:
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair
=> """

saldo = 0
limite_saque = 500
extrato = ""
LIMITE_SAQUE = 3
numero_de_saques = 0

while True:
    
    opcao = int(input(menu))
    
    if opcao == 1:
        
        valor = int(input("Digite o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print(f"O saldo agora é: R${saldo:.2f}")
            
        else:
            print("Valor digitado inválido")
            
    elif opcao == 2:
        
        valor = int(input("Digite o valor do saque: "))
        
        if valor > saldo:
            print("Saldo insuficiente")
            
        elif valor > limite_saque:
            print("Ultrapassou o limite permitido")
            
        elif numero_de_saques >= LIMITE_SAQUE:
            print("O limite de saque diários já foi atingido")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_de_saques += 1
            print(f"O saldo agora é: R${saldo:.2f}")
            
        else:
            print("Valor digitado inválido")
            
    elif opcao == 3:
        print(" Extrato ".center(28, "#"))
        print(f"Não tivemos movimentações" if not extrato else extrato)
        print(f"Saldo:R${saldo:.2f}")
        print("".center(28, "#"))
        
    elif opcao == 4:
        print("Agradecemos sua preferência")
        break
    
    else:
        print("Opção inválida!")
