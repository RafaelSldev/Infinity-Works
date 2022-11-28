'''Faça um programa que recebe a altura de um triangulo em um número inteiro e imprima-o utilizando asteriscos.'''

altura = int(input('Digite um número: '))
estrela = ' * '

for i in range(altura + 1):
    print(i * estrela)
