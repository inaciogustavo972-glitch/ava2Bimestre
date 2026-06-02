def calcular_rendimento_mes(saldo_atual, deposito, taxa):
    novo_saldo = saldo_atual + deposito
    rendimento = novo_saldo * taxa
    resultado_final = novo_saldo + rendimento
    return resultado_final


def mostrar_extrato(mes_atual, valor_total):
    print("Mes", mes_atual, ": Saldo total: R$", valor_total)


def mostrar_resultado_final(total_meses, valor_final):
    print("Ao final de", total_meses, "meses, Voce tera o valor de R$:", valor_final)


aparte = float(input("Quanto vc vai depositar por mes? "))
juros = float(input("Qual a taxa de juros da poupança? "))
meses = int(input("Por quantos meses vc ira investir? "))

juros_decimal = juros / 100
total = 0

for mes in range(1, meses + 1):
    total = calcular_rendimento_mes(total, aparte, juros_decimal)
    mostrar_extrato(mes, total)

mostrar_resultado_final(meses, total)
