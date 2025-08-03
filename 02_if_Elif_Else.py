saldo = 2000
opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato: \nDigite uma opção:" ))

if opcao == 1:
    
    valor = float(input("Informe a quantia para o saque: "))
    if valor <= saldo:
     print(f"Realizando saque de R$ {valor:.2f}")
     
     saldo -= valor
    
    else:
        print("SALDO INSUFICIÊNTE!")
        
elif opcao == 2:
    print("exibindo o Extrato: ")
    
else:
 print("Opção Inválida")
 
 