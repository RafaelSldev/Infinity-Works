n = int(input("Digite o número de pessoas: "))
print(f"O número de pessoas é: {n}")

homem = 0
mulher = 0
for i in range(0, n, 1):
    s = int(input("Você é Homem(1) ou Mulher(2)?: "))
    if s == 1:
        homem += 1
    if s == 2:
        mulher += 1

print(f"Homem(s): {homem}")
print(f"Mulher(es): {mulher}")
