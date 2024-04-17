menu = """
Menu Principal

[1] - Deposito
[2] - Saque
[3] - Extrato
[0] - Sair

Escolha o servico, por favor: """

saldo = 0
limite_quantidade_diaria = 500
extrato = """"""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

while True:
    
    opcao = int(input(menu))
    
    if opcao == 1:
        print("\nDepósito")
        
        while True:
            valor = float(input("Digite o valor a qual deseja depositar: "))
            
            if valor > 0:
                print("\nValor depositado com sucesso!")
                saldo += valor
                extrato += f"\n Depósito feito de {valor}"
                print("\nRetornando ao menu principal")
                break
                
            elif valor == 0:
                    break
                    
            else:
                print("\nValor Inválido! Tente Novamente.")
        
    elif opcao == 2:
        print("\nSaque")
        
        while True:
            print(f"Saldo Disponível: {saldo}")
            valor = float(input("Digite o valor a qual deseja sacar: "))
            
            if valor > 0:
                diferenca = saldo - valor
                
                if (valor <= limite_quantidade_diaria and diferenca >= 0) and (numero_saques <= LIMITE_SAQUES_DIARIOS and diferenca >= 0):
                    
                    print("\n Saque feito com sucesso!")
                    saldo -= valor
                    numero_saques += 1
                    limite_quantidade_diaria -= valor
                    extrato += f"\n Saque feito de {valor}"
                    print("\nRetornando ao menu principal")
                    break
                    
                elif valor == 0:
                    break
                    
                else:
                    print("""Erro! Você já deve ter alcançado os seguintes requisitos:

                    1 - Valor diário atingido
                    2 - Número  máximo de saques diários atingido
                    3 - Valor excedente ao saldo disponível

                    Tente novamente, por favor\n""")
            else:
                print("\nValor Inválido! Tente Novamente.")
        
    elif opcao == 3:
        print("\nExtrato")
        print(extrato)
        print(f" Saldo Disponível: {saldo}")
        
    elif opcao == 0:
        print("Encerrando...")
        break
    
    else:
        print("Opção inválida! Tente Novamente.")