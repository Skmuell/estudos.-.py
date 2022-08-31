while True:
    valores = [int(i) for i in input().split()]

    m = max(valores)
    n = min(valores)

    if m <= 0 or n <= 0:
        break

    soma = 0
    mensagem = ''
    for i in range(n, m+1):
        soma += i
        mensagem += str(i)+" "
    print('{}Sum={}'.format(mensagem, soma))