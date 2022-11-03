'''Faça um programa que recebe o salário de um colaborador, e calcule o
reajuste segundo os critérios abaixo, que deverá exibir o novo salário, baseado no salário atual.
Salários até R$ 280,00 (incluindo): aumento de 20%,
Salários entre R$ 280,00 e R$700,00: aumento de 15%;
Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%;
Salários de R$ 1500,00 em diante: aumento de 5%;
Exemplo:ENTRADA:700.00SAÍDA:805.00'''

salário = float(input("Digite o valor do salário:R$ "))
print(f"\nSeu salário atual é:R$ {salário}")

if 0 != salário <= 280:
    reajuste = (salário * 0.2) + salário
    print(f"O valor do salário reajustado(+20%) é:R$ {reajuste:.2f} ")
elif 280 < salário <= 700:
    reajuste = (salário * 0.15) + salário
    print(f"O valor do salário reajustado(+15%) é:R$ {reajuste:.2f} ")
elif 700 < salário <= 1500:
    reajuste = (salário * 0.1) + salário
    print(f"O valor do salário reajustado(+10%) é:R$ {reajuste:.2f} ")
elif salário > 1500:
    reajuste = (salário * 0.05) + salário
    print(f"O valor do salário reajustado(+5%) é:R$ {reajuste:.2f} ")
else:
    print("ERRO")


