'''Faça um programa que receba a idade de dez pessoas e que calcule
e mostre a quantidade de pessoas com idade maior ou igual a 18 anos.'''

contador = 0
pessoa = 0
for i in range(3):
    pessoa = int(input(f'Qual a idade da {i+1}º pessoa: '))
    if pessoa >= 18:
        contador += 1

print(f'\nQuantidade de pessoas com idade maior ou igual a 18 anos: {contador}')
