#MENU
def menu():
  menu = """\n
      --------------MENU---------------

    Selecione a opção desejada:

           [D]\tDEPÓSITO      
           [W]\tSAQUE      
           [V]\tEXTRATO
           [na]\tNOVA CONTA
           [la]\tLISTAR CONTAS
           [nu]\t NOVO USUÁRIO           
      
      Aperte [Q] para encerrar a operação.
             
    """
  return input(menu)


def depositar(float_saldo, float_valor_deposito, list_extrato, /):
    if float_valor_deposito > 0:
        float_saldo += float_valor_deposito
        list_extrato += str(f'Depósito:\tR$ {float_valor_deposito}\n')
        print("\n=== Depósito realizado com sucesso! ===")

    else :
        print("\nOperação falhou! O valor informado é inválido.")

    return float_saldo, list_extrato

def sacar(*,float_saldo, float_valor_saque, list_extrato, float_valor_limit, int_quant_saques, int_limit_saques):
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
    else : 
        print("\nOperação falhou! O valor informado é inválido.")

    return float_saldo, list_extrato

def extrato(float_saldo, /, *, list_extrato):
    print("Seu extrato:")
    print(list_extrato)
    print("Seu saldo:")
    print(float_saldo)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("--- Usuário criado com sucesso! ---")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(num_agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": num_agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado! ")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

# Acessando as Opções
def main():
  AGENCIA = "0001"

  float_saldo = 2000.00
  int_quant_saques = 0
  int_limit_saques = 3
  float_valor_limit = 5000
  list_extrato = ""
  float_valor_saque = 0.00
  float_valor_deposito = 0.00
  num_agencia = "0001"
  usuarios = []
  contas = []

  while True:
      opcao = menu()
      
      if opcao == "D":
          float_valor_deposito = float(input("Valor a ser depositado: R$"))
          float_saldo, list_extrato = depositar(float_saldo, float_valor_deposito, list_extrato)

      elif opcao == "W":
          print(f"O saque não pode ser superior a R$500,00. Operações realizadas:{int_quant_saques}/{int_limit_saques}")
          float_valor_saque = float(input('Valor de saque: R$'))
          float_saldo, list_extrato = sacar(
              float_saldo=float_saldo,
              float_valor_saque=float_valor_saque,
              list_extrato=list_extrato,
              float_valor_limit=float_valor_limit,
              int_quant_saques=int_quant_saques,
              int_limit_saques=int_limit_saques,
              )
          
      elif opcao == "V":
          extrato(float_saldo, list_extrato=list_extrato)

      elif opcao == "nu":
          criar_usuario(usuarios)

      elif opcao == "na":
          numero_conta = len(contas) + 1
          conta = criar_conta(num_agencia, numero_conta, usuarios)

          if conta:
              contas.append(conta)

      elif opcao == "la":
          listar_contas(contas)

      elif opcao == "Q":
          break

      else:
          print("Operação inválida, por favor selecione novamente a operação desejada.")


main()








