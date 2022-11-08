'''É considerado aprovado,
o aluno que obtiver a nota final superior ou igual a 6,
e que tiver comparecido a um mínimo de 40 aulas'''

soma = 0
média = 0
aulas = int(input("Quantas aulas assistidas?: "))

for i in range(1, 4):
    nota = float(input(f"Digite a {i}º nota: "))

    soma += nota

média = soma / 3

if média >= 6 and aulas >= 40:
    print(F"Nota final: {média}(APROVADO(A))")
    print(F"Aulas assistida: {aulas}(APROVADO(A))")
if média < 6 or aulas < 40:
    print(F"Nota final: {média}(REPROVADO(A))")
    print(F"Aulas assistida: {aulas}(REPROVADO(A))")
