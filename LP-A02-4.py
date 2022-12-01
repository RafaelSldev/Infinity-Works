'''Uma loja tem tem uma política de descontos de acordo com o valor da compra do cliente.
Os descontos começam quando o cliente faz compras acima dos R$500. A cada 100 reais que ultrapasse esse valor,
o cliente ganhará 1% de desconto, sendo este cumulativo até o limite de 25%.
 Por exemplo: R$500 = 1% || R$600,00 = 2% … e assim por diante.
Faça um programa que desenvolva uma tabela de descontos utilizando o formato abaixo, você deve atribuir o valor de compra de cada cliente.
valor da compra – porcentagem de desconto – valor final
Exemplo:
ENTRADA:
Compra = 520,00
SAÍDA:
520,00 ( Valor da compra ) - 1% ( Porcentagem ) = 514,80 ( Valor final )'''

'''compra = float(input("Digite o valor da compra:R$ "))
porcentagem = 0
valorFinal = 0'''

'''if 500 <= compra <= 599:
    porcentagem = compra * 0.01
    valorFinal = compra - porcentagem
    print(f"R${compra} (valor da compra) – {porcentagem:.2f}% (porcentagem de desconto) = R${valorFinal:.2f}(valor "
          f"final)")'''

compra = float(input('Digite o valor da compra: '))

if 500 <= compra <= 599:
    valor_final = compra - (compra * 0.01)
    print(f'R${compra} (Valor da compra) - 1% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 600 <= compra <= 699:
    valor_final = compra - (compra * 0.02)
    print(f'R${compra} (Valor da compra) - 2% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 700 <= compra <= 799:
    valor_final = compra - (compra * 0.03)
    print(f'R${compra} (Valor da compra) - 3% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 800 <= compra <= 899:
    valor_final = compra - (compra * 0.04)
    print(f'R${compra} (Valor da compra) - 4% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 900 <= compra <= 999:
    valor_final = compra - (compra * 0.05)
    print(f'R${compra} (Valor da compra) - 5% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 1000 <= compra <= 1099:
    valor_final = compra - (compra * 0.06)
    print(f'R${compra} (Valor da compra) - 6% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 1100 <= compra <= 1199:
    valor_final = compra - (compra * 0.07)
    print(f'R${compra} (Valor da compra) - 7% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 1200 <= compra <= 1299:
    valor_final = compra - (compra * 0.08)
    print(f'R${compra} (Valor da compra) - 8% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 1300 <= compra <= 1399:
    valor_final = compra - (compra * 0.09)
    print(f'R${compra} (Valor da compra) - 9% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 1400 <= compra <= 1499:
    valor_final = compra - (compra * 0.1)
    print(f'R${compra} (Valor da compra) - 10% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 1500 <= compra <= 1599:
    valor_final = compra - (compra * 0.11)
    print(f'R${compra} (Valor da compra) - 11% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 1600 <= compra <= 1699:
    valor_final = compra - (compra * 0.12)
    print(f'R${compra} (Valor da compra) - 12% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 1700 <= compra <= 1799:
    valor_final = compra - (compra * 0.13)
    print(f'R${compra} (Valor da compra) - 13% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 1800 <= compra <= 1899:
    valor_final = compra - (compra * 0.14)
    print(f'R${compra} (Valor da compra) - 14% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 1900 <= compra <= 1999:
    valor_final = compra - (compra * 0.15)
    print(f'R${compra} (Valor da compra) - 15% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 2000 <= compra <= 2000:
    valor_final = compra - (compra * 0.16)
    print(f'R${compra} (Valor da compra) - 16% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 2100 <= compra <= 2199:
    valor_final = compra - (compra * 0.17)
    print(f'R${compra} (Valor da compra) - 17% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 2200 <= compra <= 2299:
    valor_final = compra - (compra * 0.18)
    print(f'R${compra} (Valor da compra) - 18% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 2300 <= compra <= 2399:
    valor_final = compra - (compra * 0.19)
    print(f'R${compra} (Valor da compra) - 19% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 2400 <= compra <= 2499:
    valor_final = compra - (compra * 0.2)
    print(f'R${compra} (Valor da compra) - 20% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 2500 <= compra <= 2599:
    valor_final = compra - (compra * 0.21)
    print(f'R${compra} (Valor da compra) - 21% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 2600 <= compra <= 2699:
    valor_final = compra - (compra * 0.22)
    print(f'R${compra} (Valor da compra) - 22% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 2700 <= compra <= 2799:
    valor_final = compra - (compra * 0.23)
    print(f'R${compra} (Valor da compra) - 23% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 2800 <= compra <= 2899:
    valor_final = compra - (compra * 0.24)
    print(f'R${compra} (Valor da compra) - 24% (Porcentagem): R${valor_final:.2f} (Valor final)')

if 2900 <= compra <= 2999:
    valor_final = compra - (compra * 0.25)
    print(f'R${compra} (Valor da compra) - 25% (Porcentagem): R${valor_final:.2f} (Valor final)')
