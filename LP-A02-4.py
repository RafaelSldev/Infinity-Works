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

for i in range(500, 2600, 100):
    for j in range(1, 26, 1):
        print(i, j)
