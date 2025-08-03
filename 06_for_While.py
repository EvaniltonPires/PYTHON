
opcao = -1

while opcao != 0:
    print("Escolha uma OPÇÃO")
    opcao = int(input("[1] SACAR \n[2] EXTRATO \n[0] SAIR\n"))

    if opcao == 1:
        print("SACANDO...")

    elif opcao == 2:
        print("Exibindo Extrato")

    elif opcao == 0:
        print("Obrigado por utilizar nosso Sistema Bancário")

    else:
        print("Opção inválida. Tente novamente.")
