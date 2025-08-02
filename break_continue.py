while True :
    print("Escolha uma Opção:")

    opcao = int(input("[1] SACAR \n[2] EXTRATO \n[0] SAIR\n"))

    if opcao == 1:
        print("Sacando...\n")
        continue #volta para  o ínicio do loop

    elif opcao == 2:
        print("Exibindo Extratos")
        continue # volta para o ínicio do loop

    elif opcao == 0:
        print("Obrigado por utilizar nosso Sistema Bancário")
        break # encerra o loop

    else:
        print("Opção inválida! Tente novamente.\n")
        continue # volta para o ínicio do loop
