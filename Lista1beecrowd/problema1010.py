linha1 = input().split()
linha2 = input().split()

valorpeca1 = int(linha1[1])*float(linha1[2])
valorpeca2 = int(linha2[1])*float(linha2[2])

compra = valorpeca1 + valorpeca2

print("VALOR A PAGAR: R$ %.2f" %compra)
