menu = """
###################### D BANK ######################

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

>>> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)
  
  if opcao == "d":
    valor_deposito = float(input("""
################ Operação: Depósito ################
Digite o valor desejado

>>> """))
    if valor_deposito > 0:
      saldo += valor_deposito
      print("\nDepósito realizado com sucesso!")
      print(f"Saldo atual: R${saldo:.2f}")
      extrato += f"Depósito realizado no valor de: {valor_deposito}R$\n"
    else:
      print("\nValor do depósito precisa ser positivo")
  elif opcao == "s":
    valor_saque = float(input("""
### Operação: Depósito ###
Digite o valor desejado

>>> """))
    if valor_saque <= 0:
      print("\nOperação falhou! Valor de saque negativo ou zerado")
    if valor_saque > saldo:
      print("\nOperação falhou! Valor de saque maior que o saldo.")
      print(f"Valor do saque: {valor_saque} R$\nSaldo atual: {saldo:.2f} R$")
    elif numero_saques >= LIMITE_SAQUES:
      print("\nOperação falhou! Você antigiu o número máximo de saques diários.")
      print(f"Número de saques: {numero_saques}")
    else:
      print("\nSaque realizado com sucesso!")
      saldo -= valor_saque
      numero_saques += 1
      print(f"Valor do saque: {valor_saque} R$\nSaldo atual: {saldo:.2f} R$")
      extrato += f"Saque realizado no valor de: {valor_saque}R$\n"
  
  elif opcao == "e":
    print("\n#################### EXTRATO #####################\n")
    print("Ainda não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: {saldo:.2f} R$\n")
    print("####################################################")

  elif opcao == "q":
    print("Obrigado por utilizar nossos serviços!")
    print("Sessão expirada com sucesso.")
    break
  else:
    print("Operação inválida, por favor tente novamente.")