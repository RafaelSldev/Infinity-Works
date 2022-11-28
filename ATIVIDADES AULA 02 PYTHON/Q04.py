'''Escreva um programa que recebe inteiro e
mostra os números pares e ímpares (separados), de 1 até esse inteiro.'''

n = int(input('Digite um numero inteiro: '))

print('*** Números Pares ***')
for i in range(1, n+1):
    if i % 2 == 0:
        print(i, end=' ')
print('\n\n*** Números Ímpares ***')
for i in range(1, n+1):
    if i % 2 == 1:
        print(i, end=' ')
