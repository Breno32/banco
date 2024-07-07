menu = """

[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(print("informe o valor do deposito"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("operacao falhou")

    elif opcao == "s":
        valor = float(print("Informe o valor do saque"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("operacao falhou! Voce nao tem saldo o suficiente.")

        elif excedeu_limite:
            print("operacao falho! o valor de saque excede o limite.")

        elif excedeu_saques:
            print("operacao falhou! numero maximo de saques exedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("operacao falhou! o valor informado e invalido.")
    
    
    elif opcao == "e":
        print("\n=========Extrato========")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================")

    elif opcao == "q":
        break

    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada.")


   
        
    
