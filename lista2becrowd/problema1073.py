x = int(input())
y = 2

for i in range(1, x + 1):
    if i %2 == 0:
        print("{}^2 = {}".format(i, i**2))