#MENU
menu_conta = """
      -------MENU--------

    Selecione a opção desejada:

           [D]DEPÓSITO
      
           [W]SAQUE
      
           [V]EXTRATO
      
      Aperte [Q] para encerrar a operação.
             
    """
# Controles de Status da Conta
float_saldo = 2000.00
int_quant_saques = 0
int_limit_saques = 3
float_valor_limit = 500.00
list_extrato = str()
float_valor_saque = 0.00
float_valor_deposito = 0.00
# Acessando as Opções
while True:   

    str_opcao_escolhida = input(menu_conta)

    if str_opcao_escolhida == "W":
        print(f"O saque não pode ser superior a R$500,00. Operações realizadas:{int_quant_saques}/{int_limit_saques}")
        float_valor_saque = float(input('Valor de saque: R$'))
        excedeu_saldo = float_valor_saque > float_saldo
        excedeu_limite_saque = int_quant_saques > int_limit_saques 
        excedeu_valor_saque = float_valor_saque > float_valor_limit
        if excedeu_saldo:
            print("Saldo indisponível!")
        elif excedeu_limite_saque:
            print("Limite de saque diário atingido!")
        elif excedeu_valor_saque:
            print("Valor limite por operação atingido!")
        elif float_valor_saque > 0:
            print("Retire o seu dinheiro.")
            float_saldo -= float_valor_saque
            int_quant_saques += 1
            list_extrato += str(f'Saque: R$ {float_valor_saque}\n')
    
    elif str_opcao_escolhida == "D":
        float_valor_deposito = float(input("Valor a ser depositado: R$"))
        float_saldo += float_valor_deposito
        list_extrato += str(f'Depósito: R$ {float_valor_deposito}\n')
    
    elif str_opcao_escolhida == "V":
        print("Seu extrato:")
        print(list_extrato)
        print("Seu saldo:")
        print(float_saldo)
    elif str_opcao_escolhida == "Q":
        break
    else:
        print("Operação cancelada!")









