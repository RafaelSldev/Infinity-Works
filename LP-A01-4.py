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
