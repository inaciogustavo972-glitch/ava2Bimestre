def calcular_imc(p, a):
    resultado = p / (a * a)
    return resultado


def classificar(valor_imc):
    if valor_imc < 25:
        return "NORMAL"
    else:
        return "ACIMA DO PESO"


def gerar_aviso(status):
    if status == "NORMAL":
        return "Muito bem! Continue mantendo uma alimentacao saudavel e praticando exercicios."
    else:
        return "Atencao! Tente incluir mais alimentos naturais na sua rotina e faca caminhadas."


peso_texto = input("Digite o seu peso em kg (ex: 70 ou 70.5): ")
peso_texto = peso_texto.replace(",", ".")
peso_usuario = float(peso_texto)

altura_texto = input("Digite a sua altura em metros (ex: 1.75 ou 1,75): ")
altura_texto = altura_texto.replace(",", ".")
altura_usuario = float(altura_texto)

imc_final = calcular_imc(peso_usuario, altura_usuario)
status_final = classificar(imc_final)
dica_final = gerar_aviso(status_final)

print("--- AVALIADOR DE SAUDE INTELIGENTE ---")
print("Seu IMC e:", imc_final)
print("Sua classificacao e:", status_final)
print("Recomendacao:", dica_final)
