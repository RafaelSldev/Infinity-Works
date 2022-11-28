dia = int(input('Digite o dia do seu nascimento: '))
mes = str(input('Digite o mes do seu nascimento: ')).lower()

if 20 < dia < 31 and mes == 'março' or 1 < dia < 21 and mes == 'abril':
    print('Áries')

if 20 < dia < 30 and mes == 'abril' or 1 < dia < 21 and mes == 'maio':
    print('Touro')

if 20 < dia < 31 and mes == 'maio' or 1 < dia < 21 and mes == 'junho':
    print('Gêmeos')

if 20 < dia < 30 and mes == 'junho' or 1 < dia < 23 and mes == 'julho':
    print('Câncer')

if 22 < dia < 31 and mes == 'julho' or 1 < dia < 23 and mes == 'agosto':
    print('Leão')

if 22 < dia < 31 and mes == 'agosto' or 1 < dia < 24 and mes == 'setembro':
    print('Virgem')

if 22 < dia < 30 and mes == 'setembro' or 1 < dia < 23 and mes == 'outubro':
    print('Libra')

if 22 < dia < 31 and mes == 'outubro' or 1 < dia < 22 and mes == 'novembro':
    print('Escorpião')

if 21 < dia < 30 and mes == 'novembro' or 1 < dia < 22 and mes == 'dezembro':
    print('Sagitário')

if 21 < dia < 31 and mes == 'Dezembro' or 1 < dia < 21 and mes == 'Janeiro':
    print('Capricórnio')

if 20 < dia < 31 and mes == 'janeiro' or 1 < dia < 19 and mes == 'fevereiro':
    print('Aquário')

if 18 < dia < 29 and mes == 'fevereiro' or 1 < dia < 21 and mes == 'março':
    print('Peixes')
