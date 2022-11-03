'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
imposto de renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
e que o FGTS corresponde a 11% do salário bruto, mas não é descontado (é a empresa que deposita.)
O salário líquido corresponde ao salário bruto menos os descontos. O programa deverá pedir ao usuário
o valor da sua hora e a quantidade de horas trabalhadas no mês.
a. Desconto do IR;
b. Salário Bruto ate R$900,00 (inclusive) – Isento;
c. Salário Bruto de R$ 1500, 00 (inclusive) – desconto de 5%;
d. Salario bruto até R$ 2500,00 (Inclusive) – desconto de 10%;
e. Salário bruto acima de 2500 – Desconto de 20%.
Imprima na tela as informações, dispostas conforme o exemplo abaixo,
no exemplo valor da hora é 5 e a quantidade de horas é 220.
Salário bruto (5 * 220): R$ 1100,00
( – ) IR (5%): R$ 55,00
( – ) INSS ( 10% ): R$ 110,00
( – ) Sindicato(3%): R$ 33,00
FGTS (11%): R$ 121,00
Total de descontos: R$ 198,00
Salário Líquido: R$ 902,00'''





valor_daHora_trabalhada = int(input("Digite o valor da hora trabalhada: "))
hora_trabalhada = int(input("Digite a quantidade de horas trabalhadas no mês: "))
salário_bruto = valor_daHora_trabalhada * hora_trabalhada
descontos = 0
salário_liquido = 0
print(f"\nSalário Bruto:R$ {salário_bruto}")

if 0 != salário_bruto <= 900:
    ir = float(0)
    print(f"( – ) IR (0%):R$ {ir}(ISENTO)")
elif 1500 >= salário_bruto > 900:
    ir = salário_bruto * 0.05
    print(f"( – ) IR (5%):R$ {ir}")
elif 1500 < salário_bruto <= 2500:
    ir = salário_bruto * 0.1
    print(f"( – ) IR (10%):R$ {ir}")
elif salário_bruto > 2500:
    ir = salário_bruto * 0.2
    print(f"( – ) IR (20%):R$ {ir}")
else:
    print("ERRO")

inss = salário_bruto * 0.1
sindicato = salário_bruto * 0.03
fgts = salário_bruto * 0.11
descontos = ir + inss + sindicato
salário_liquido = salário_bruto - descontos

print(f"( – ) INSS (10%):R$ {inss}")
print(f"( – ) Sindicato(3%):R$ {sindicato:.2f}")
print(f"FGTS (11%):R$ {fgts}")
print(f"Total de descontos:R$ {descontos}")
print(f"Salário Líquido:R$ {salário_liquido}")
