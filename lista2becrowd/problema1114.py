senha = 2002
while True:
    while True:
        try:
            entrada = int(input())
            break
        except ValueError:
            print("Senha Invalida")
    if entrada == senha:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")