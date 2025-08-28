# Importa o módulo time (usado apenas se você quiser adicionar delays, aqui está por padrão)
import time

# Cria uma lista para armazenar os cálculos feitos anteriormente (histórico em memória)
historico = []

# Função para converter a dose prescrita para miligramas
def converter_para_mg(valor, unidade):
    unidade = unidade.lower()  # Converte a unidade para minúsculas, para evitar erros de digitação

    # Se a unidade for grama, converte para miligrama (1g = 1000mg)
    if unidade == "g":
        return valor * 1000
    # Se já estiver em mg, retorna o mesmo valor
    elif unidade == "mg":
        return valor
    # Se for micrograma (mcg), converte para mg (1000mcg = 1mg)
    elif unidade == "mcg":
        return valor / 1000
    # Se a unidade for inválida, lança um erro
    else:
        raise ValueError("Unidade inválida para dose prescrita.")

# Função para converter a concentração para mg/ml
def converter_para_mg_por_ml(valor, unidade):
    unidade = unidade.lower()  # Converte a unidade para minúsculas

    # Se já estiver em mg/ml, retorna o valor
    if unidade == "mg/ml":
        return valor
    # Se for g/ml, converte para mg/ml (1g = 1000mg)
    elif unidade == "g/ml":
        return valor * 1000
    else:
        raise ValueError("Unidade inválida para concentração.")

# Função que realiza o cálculo da dosagem
def calcular_dosagem(dose_prescrita, un_dose, concentracao, un_conc):
    # Converte a dose prescrita para mg
    dose_mg = converter_para_mg(dose_prescrita, un_dose)
    # Converte a concentração para mg/ml
    conc_mg_ml = converter_para_mg_por_ml(concentracao, un_conc)

    # Garante que a concentração não seja zero (evita divisão por zero)
    if conc_mg_ml == 0:
        raise ValueError("A concentração não pode ser zero.")

    # Calcula o volume em ml a ser administrado (dose em mg dividido pela concentração)
    volume_ml = dose_mg / conc_mg_ml
    return dose_mg, volume_ml  # Retorna a dose em mg e o volume em ml

# Função para mostrar o histórico de cálculos feitos
def mostrar_historico():
    if not historico:
        print("\n Nenhum cálculo realizado ainda.")  # Se não houver histórico
    else:
        print("\n Histórico de cálculos:")
        for item in historico[-10:]:  # Mostra os últimos 10 registros
            print(f"- {item}")

# Função principal que roda o sistema
def main():
    print(" Bem-vindo ao DoseCerta - Calculadora de Dosagem Médica")

    while True:  # Loop principal que continua até o usuário decidir sair
        try:
            print("\nInsira os dados da prescrição:")

            # Recebe a dose prescrita (ex: 1)
            dose = float(input("➡️  Dose prescrita (ex: 1): "))
            # Recebe a unidade da dose (ex: g, mg, mcg)
            un_dose = input("➡️  Unidade da dose (g, mg, mcg): ")

            # Recebe a concentração do medicamento (ex: 500)
            concentracao = float(input("➡️  Concentração do medicamento (ex: 500): "))
            # Recebe a unidade da concentração (ex: mg/ml ou g/ml)
            un_conc = input("➡️  Unidade da concentração (mg/ml ou g/ml): ")

            # Chama a função para calcular a dose e o volume
            dose_mg, volume_ml = calcular_dosagem(dose, un_dose, concentracao, un_conc)

            # Mostra os resultados para o usuário
            print(f"\n Dose convertida: {dose_mg:.2f} mg")
            print(f" Você deve administrar: {volume_ml:.2f} ml")

            # Verifica e exibe alertas se o volume estiver muito alto ou baixo
            if volume_ml > 10:
                print(" Alerta: volume elevado, revise a prescrição.")
            elif volume_ml < 0.5:
                print(" Alerta: volume muito pequeno, atenção à precisão.")

            # Salva o cálculo no histórico
            registro = f"{dose}{un_dose} → {volume_ml:.2f} ml"
            historico.append(registro)

        # Captura erros de conversão ou entrada incorreta de unidade
        except ValueError as ve:
            print(f" Erro: {ve}")
        # Captura qualquer outro erro inesperado
        except Exception as e:
            print(f" Erro inesperado: {e}")

        # Pergunta ao usuário se deseja continuar ou encerrar
        opcao = input("\nDeseja realizar outro cálculo? (s/n/ver histórico): ").lower()

        # Encerra o programa se a resposta for "n"
        if opcao == "n":
            print("👋 Encerrando o sistema. Até logo!")
            break
        # Mostra o histórico se o usuário pedir
        elif opcao == "ver histórico":
            mostrar_historico()
            input("\nPressione Enter para continuar...")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
