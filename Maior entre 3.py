a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

if b < a > c:
    print(f"\n{a} é o maior número.")
if a < b > c:
    print(f"\n{b} é o maior número.")
elif a < c > b:
    print(f"\n{c} é o maior número.")
