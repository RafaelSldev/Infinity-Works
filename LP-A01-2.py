'''Sendo assim, faça um programa que
leia um número de ponto flutuante (Número Real) e
mostre na tela o seu dobro e a sua terça parte.

Exemplo:ENTRADA:Número: 2.5SAÍDA:Dobro: 5.0Terça Parte: 0,83'''


numero = float(input("Digite um número real: "))
dobro = numero * 2
terça_parte = numero / 3

print(f"\nDobro:{dobro} \nTerça Parte : {terça_parte:.2f}")
