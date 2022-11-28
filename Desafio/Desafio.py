'''Desafio: Um posto está vendendo combustíveis com a seguinte tabela de descontos: Álcool:
Até 20 litros: desconto de 3% por litro
Acima de 20 litros: Desconto de 5% por litro 99.

Gasolina:
Até 20 litros: desconto de 4% por litro
Acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool. G-gasolina), calcule e imprima o valor a ser pago pelo cliente.'''
import os
os.system('clear')

combustivel = str(
    input("Qual o seu combustível? A-Álcool G-Gasolina: ")).upper()

valor_pago = 0
valor_inicial = 0

match combustivel:
    case 'A':
        print("\nCombustível: Álcool | Valor do litro RS4,00")
        litros_al = int(input("\nQuantos litros?: "))
        if litros_al <= 20:
            valor_inicial = litros_al * 4
            valor_pago = valor_inicial - (valor_inicial * 0.03)
            print(
                f"\nValor pago:R$ {valor_pago} ({litros_al}litros(-3% Desconto por litro))\n\n")
        elif litros_al > 20:
            valor_inicial = litros_al * 4
            valor_pago = valor_inicial - (valor_inicial * 0.05)
            print(
                f"\nValor pago:R$ {valor_pago} ({litros_al}litros(-5% Desconto por litro))\n\n")

    case 'G':
        print("\nCombustível: Gasolina | Valor do litro RS5,00")
        litros_gs = int(input("\nQuantos litros?: "))
        if litros_gs <= 20:
            valor_inicial = litros_gs * 5
            valor_pago = valor_inicial - (valor_inicial * 0.04)
            print(
                f"\nValor pago:R$ {valor_pago} ({litros_gs}litros(-4% Desconto por litro))\n\n")
        elif litros_gs > 20:
            valor_inicial = litros_gs * 5
            valor_pago = valor_inicial - (valor_inicial * 0.06)
            print(
                f"\nValor pago:R$ {valor_pago} ({litros_gs}litros(-6% Desconto por litro))\n\n")
