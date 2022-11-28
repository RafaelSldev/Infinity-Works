anos = int(input('Digite a sua idade: '))
meses = int(input('Quantos meses?: '))
dias = int(input('Quanto(s) dia(s): '))

soma_ano = anos * 365
soma_mes = meses * 30

soma_total = soma_ano + soma_mes + dias

print(f'Sua idade em dias é: {soma_total}')
