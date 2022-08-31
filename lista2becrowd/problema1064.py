quantidade = 0
soma = 0

for x in range(6):
    valor = float(input())
    if valor > 0:
        quantidade = quantidade +1
        soma += valor
media = soma / quantidade 

print(quantidade, "valores positivos")
print("%.1f" % media)
