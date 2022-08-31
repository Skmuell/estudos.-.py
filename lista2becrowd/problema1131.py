grenal = 0
vitoria_inter = 0
vitoria_gremio = 0
empate = 0

while True:
    inter, gremio = [int(gol) for gol in input().split()]
    if inter > gremio:
        vitoria_inter += 1
    elif gremio > inter:
        vitoria_gremio += 1
    else:
        empate += 1
    grenal += 1
    print("Novo grenal (1-sim 2-nao)")
    jogo = int(input())
    if jogo == 1:
        continue
    else: 
        break

print("{} grenais".format(grenal))
print("Inter:{}".format(vitoria_inter))
print("Gremio:{}".format(vitoria_gremio))
print("Empates:{}".format(empate))

if vitoria_inter > vitoria_gremio:
    print("Inter venceu mais")
elif vitoria_inter < vitoria_gremio:
    print("Gremio venceu mais")
else:
    print("Não houve vencedor")