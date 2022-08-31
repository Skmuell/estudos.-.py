c = r = s = 0
n = int(input())
for i in range(n):
    opc = input().split()
    num, bicho = opc
    if bicho.upper() == 'C':
        c += int(num)
    elif bicho.upper() == 'R':
        r += int(num)
    elif bicho.upper() == 'S':
        s += int(num)

total = c + r + s

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(c))
print('Total de ratos: {}'.format(r))
print('Total de sapos: {}'.format(s))
print('Percentual de coelhos: {:.2f} %'.format(c / total * 100))
print('Percentual de ratos: {:.2f} %'.format(r / total * 100))
print('Percentual de sapos: {:.2f} %'.format(s / total * 100))
