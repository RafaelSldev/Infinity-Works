vazamento = int(input('Vazamentos: '))
somaLitros = 0
soma = 0
for i in range(0, vazamento):
    litros_hora = int(input('Litros por hora: '))
    hora = int(input('Horas: '))
    somaLitros = litros_hora * hora
    soma += somaLitros

print(soma, 'Litros')
