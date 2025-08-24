
# Tipos de contas
CONTA_NORMAL = 1
CONTA_UNIVERSITARIA = 2

# Dados do cliente
tipo_conta = int(input("Informe o tipo de conta: \n[1] Conta Normal \n[2] Conta Universitária\nDIGITE UMA OPÇÃO: "))
saldo = 10000
cheque_especial = 450
saque = float(input("Informe o valor do saque: "))

if tipo_conta == CONTA_NORMAL:
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com sucesso usando o cheque especial.")
    else:
        print("Saldo insuficiente, mesmo com cheque especial.")

elif tipo_conta == CONTA_UNIVERSITARIA:
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    else:
        print("Saldo insuficiente. Conta universitária não possui cheque especial.")

else:
    print("Tipo de conta inválido.")
