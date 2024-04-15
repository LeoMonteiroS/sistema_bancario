menu = """

[1] Depósito
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        print("Depósito")
        print("-"*30)
        valor = float(input("\n Digite o valor do seu depsito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} \n"
        else:
            print("Operação falhou! O valor informado é inválido")
        
    elif opcao == "2":
        print("Sacar")
        print("-"*30)
        valor = float(input("\n Digite o valor que deseja sacar: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >=LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falho! Você não tem saldo usuficiente. ")
        elif excedeu_limite:
            print("Operação falhou! O valor de saque excede o limite. ")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido. ")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválida")
        
    elif opcao == "3":
        print("\n****************Extrato****************")
        print("Não foram realizado movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("******************************************")
        
        
    elif opcao == "4":
        break
        
    else:
        print("Operação falhou! O valor informado é inválida")