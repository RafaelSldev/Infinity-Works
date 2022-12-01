n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))

for i in range(n1, n2):
    contador = 0
    for j in range(1, i + 1):
        if i % j == 0:
            contador += 1
    if contador == 2:
        print(i, end=' ')
