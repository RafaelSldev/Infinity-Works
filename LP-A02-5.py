i = int(input("Digite um número: "))
fatorial = 1
print(f'{i}!= ', end='')

for i in range(i, 0, -1):
    fatorial *= i
    print(f'{i}', end=' ')
    print('* ' if i > 1 else '=', end='')
print(f' {fatorial}')
