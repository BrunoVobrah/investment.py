def calcular_rendimento_investimento(investimento_inicial, aportes_mensais, taxa_juros, tempo_meses):
    saldo = investimento_inicial
    for mes in range(1, tempo_meses + 1):
        saldo *= (1 + taxa_juros)
        saldo += aportes_mensais
        print(f"Após {mes} meses, o saldo é de R${saldo:.2f}")
    return saldo

# Pedindo as informações ao usuário
investimento_inicial = float(input("Digite o valor do investimento inicial: R$"))
aportes_mensais = float(input("Digite o valor dos aportes mensais: R$"))
taxa_juros = float(input("Digite a taxa de juros mensal (em decimal): "))
tempo_meses = int(input("Digite a quantidade de meses que deseja calcular: "))

saldo_final = calcular_rendimento_investimento(investimento_inicial, aportes_mensais, taxa_juros, tempo_meses)
print(f"\nO saldo final após {tempo_meses} meses é de R${saldo_final:.2f}")