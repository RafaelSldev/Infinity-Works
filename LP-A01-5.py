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


