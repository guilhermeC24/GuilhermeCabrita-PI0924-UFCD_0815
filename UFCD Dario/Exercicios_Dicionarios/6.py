vendas = {"Janeiro": 1000, "Fevereiro": 1500, "Março": 1200}

dinheirito_total = 0

for mes, massa in vendas.items():
    dinheirito_total += massa

print("Total do trimestre:", dinheirito_total)