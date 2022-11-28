n = int(input('Digite um número entre 1 e 100: '))
contador = 0

for i in range(1, n+1):
    if n % i == 0:
        contador += 1

if contador == 2:
    print('Número primo')
else:
    print('Não é primo')
