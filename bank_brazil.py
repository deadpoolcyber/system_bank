menu = """
Bem-vindo ao Bank Brazil
Qual operação deseja fazer?

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
#Depositar
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
              
        else:
            print("Operação falhou! O valor informado é inválido.")
#Sacar
    elif opcao == "2":
        valor = float(input("Qual o valor que deseja sacar?: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Desculpe! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Desculpe! Seu saldo de saques é de R$ 500,00")

        elif excedeu_saques:
            print("Desculpe! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
#Extrato
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break
        

    else:
        print("Opção Invalida")