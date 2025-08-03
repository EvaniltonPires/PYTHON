# Projeto: Menu de Exercícios de Estruturas Condicionais e Repetição

def verificacao_numero():
    num = int(input("Digite um número inteiro: "))

    if num > 0 :
        print("POSITIVO")

    elif num < 0:
        print("NEGATIVO")

    else:
        print("ZERO")

def soma_1_10():
    soma = 0
    for i in range(1,11):
        soma += i
    print(f"Soma dos números de 1 a 10: {soma}")


def chute_numero():
    numero_secreto = 7
    while True:
        chute = int(input("Tente adivinhar um número sercreto de 1 a 10"))

        if chute == numero_secreto:
            print("Parabéns, Você acertou")
            break
        else:
            print(" Errado, tente novamente")


def par_ou_impar():
    num = int(input(" Digite um número: "))
    resultado = "par" if num % 2 == 0 else "impar"
    print(resultado)

def for_com_break_continue():
    for i in range(1, 21):
        if i > 15:
            print("Número maior que 15, encerrando o laço.")
            break
        if i % 3 == 0:
            print(f"pulei o número {i}")
            continue
        print(i)


def menu():
    while True:
        print("\nMenu de Exercícios")
        print("1 - Verifica número positivo, negativo ou zero")
        print("2 - Soma números de 1 a 10")
        print("3 - Jogo de adivinhar número")
        print("4 - Verifica par ou ímpar")
        print("5 - Laço com break e continue")
        print("0 - Sair")

        escolha = input("Escolha uma opção:")

        if escolha == "1":
            verificacao_numero()
        elif escolha == "2":
            soma_1_10()
        elif escolha == "3":
            chute_numero()
        elif escolha == "4":
            par_ou_impar()
        elif escolha == "5":
            for_com_break_continue()
        elif escolha == "0":
            print("SAINDO DO PROGRAMA")
            break

        else:
            print("Opção Inválida, Tente novamente.")

            if __name__ == "__main__":
                menu()
