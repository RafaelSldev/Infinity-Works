idade = 0
qt_15 = 0
qt_16a30 = 0
qt_31a45 = 0
qt_46a60 = 0
acm_61 = 0

for i in range(0, 15):
    idade = int(input("Qual a sua idade?: "))
    if idade <= 15:
        qt_15 += 1
    if 16 <= idade <= 30:
        qt_16a30 += 1
    if 31 <= idade <= 45:
        qt_31a45 += 1
    if 46 <= idade <= 60:
        qt_46a60 += 1
    if 61 <= idade:
        acm_61 += 1
print(f"A quantidade de pessoa até 15 anos é: {qt_15}")
print(f"A quantidade de pessoa de 16 a 30 anos é: {qt_16a30}")
print(f"A quantidade de pessoa de 31 a 45 anos é: {qt_31a45}")
print(f"A quantidade de pessoa de 46 a 60 anos é: {qt_46a60}")
print(f"A quantidade de pessoa acima de 61 anos é: {acm_61}")

perc_prima = (qt_15 + acm_61) / 15
print(f"A percentagem de pessoas na primeira e na última faixa etária, com relação ao total de pessoas é: {perc_prima:.2f} %")
