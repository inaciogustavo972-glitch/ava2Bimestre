# Programador 1: Lógica Matemática
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Programador 2: Classificação de Dados
def classificar(valor_imc):
    if valor_imc < 25:
        return "NORMAL"
    else:
        return "ACIMA DO PESO"

# Programador 3: Especialista em Conteúdo
def gerar_aviso(status):
    if status == "NORMAL":
        return "Continue mantendo hábitos saudáveis, como uma dieta equilibrada e exercícios regulares."
    elif status == "ACIMA DO PESO":
        return "Que tal incluir mais atividades físicas na sua rotina e consultar um nutricionista para reavaliar a dieta?"

# Programador 4: Engenheiro de Integração (Fluxo Principal)
def main():
    # Solicitando dados ao usuário
    try:
        peso = float(input("Digite o seu peso (em kg): "))
        altura = float(input("Digite a sua altura (em metros): "))
        
        # Chamando as funções na ordem correta
        imc_calculado = calcular_imc(peso, altura)
        status_imc = classificar(imc_calculado)
        aviso = gerar_aviso(status_imc)
        
        # Exibindo os resultados finais
        print("\n--- Resultados ---")
        print(f"IMC Calculado: {imc_calculado:.2f}")
        print(f"Classificação: {status_imc}")
        print(f"Recomendação: {aviso}")
        
    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos para peso e altura.")

# Execução do programa
if __name__ == "__main__":
    main()

