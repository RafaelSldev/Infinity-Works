'''Assim o Flash pediu para que você crie um programa que calcule
sua velocidade dado o espaço e o tempo.A Velocidade pode ser calculada pela fórmula:

Velocidade = Espaço / Tempo
Entrada: Seu programa deve receber dois números inteiros o espaço e o tempo,
respectivamente.Saída: A saída consiste em uma única linha contendo a velocidade
alcançada.

Exemplo:ENTRADA:Espaço: 100Tempo: 10SAÍDA:Velocidade: 10'''

espaço = int(input("Qual o valor do espaço?: "))
tempo = int(input("Qual o valor do tempo?: "))

velocidade = espaço / tempo

print(f"\nA velocidade do flash é: {velocidade}")
