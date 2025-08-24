# Função para obter um valor numérico positivo (com validação)

def obter_valor_positivo(tipo_unidade):
    while True:
        entrada = input(f"Digite um valor em {tipo_unidade}: ")
        try:
            valor = float(entrada)  # Tenta converter para número
            if valor > 0:
                return valor  # Retorna apenas se for positivo
            else:
                print(f"Erro! O valor em {tipo_unidade} deve ser maior que 0. Tente novamente.")
        except ValueError:
            print("Erro! Por favor, insira um valor numérico válido.")

# Função para obter qualquer valor numérico (para Celsius, pode ser negativo)
def obter_valor_numerico(tipo_unidade):
    while True:
        entrada = input(f"Digite a temperatura em {tipo_unidade}: ")
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print("Erro! Por favor, insira um valor numérico válido.")

# Conversão de gramas para miligramas
def converter_gramas_para_miligramas():
    gramas = obter_valor_positivo("gramas")
    miligramas = gramas * 1000
    print(f"A conversão de {gramas} gramas para miligramas é {miligramas:.2f} mg.\n")


# Conversão de litros para mililitros
def converter_litros_para_mililitros():
    litros = obter_valor_positivo("litros")
    mililitros = litros * 1000
    print(f"A conversão de {litros} litros para mililitros é {mililitros:.2f} ml.\n")
    

# Conversão de km para metros
def converter_km_para_metros():
    km = obter_valor_positivo("quilômetros")
    metros = km * 1000
    print(f"A conversão de {km} km para metros é {metros:.2f} m.\n")

# Conversão de Celsius para Fahrenheit
def converter_celsius_para_fahrenheit():
    celsius = obter_valor_numerico("Celsius")
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.2f}°C é equivalente a {fahrenheit:.2f}°F.\n")

# Exibição do menu principal
def exibir_menu():
    print("=== Conversor de Unidades ===")
    print("1 - Converter gramas para miligramas")
    print("2 - Converter litros para mililitros")
    print("3 - Converter quilômetros para metros")
    print("4 - Converter Celsius para Fahrenheit")
    print("5 - Sair")

# Loop principal do programa
while True:
    exibir_menu()  # Mostra o menu
    escolha = input("Escolha uma opção (1 a 5): ")

    # Verifica a opção escolhida e executa a função correspondente
    if escolha == "1":
        converter_gramas_para_miligramas()
    elif escolha == "2":
        converter_litros_para_mililitros()
    elif escolha == "3":
        converter_km_para_metros()
    elif escolha == "4":
        converter_celsius_para_fahrenheit()
    elif escolha == "5":
        print("Saindo do programa. Obrigado!")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção entre 1 e 5.\n")
