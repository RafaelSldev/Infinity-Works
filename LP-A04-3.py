waze = str(input('Qual a direção: ')).lower()
contador = 0
soma = 0

while waze != 'parar':
    waze = str(input('Qual a direção: ')).lower()
    contador += 100

soma = contador / 1000

print(f'\nA distância percorrida foi: {soma}km')
