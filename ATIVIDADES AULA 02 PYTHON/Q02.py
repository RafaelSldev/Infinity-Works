'''Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja foi superior a loja B (faturamento = 54000).
Se o faturamento atingir esse valor mostre na tela uma mensagem contendo em quanto foi superado o faturamento.'''

soma = 0
for i in range(5):
    cliente = int(input(f'Digite o faturamento do {i+1}º cliente: '))
    soma += cliente

if soma > 54000:
    diferença = soma - 54000
    print(f'Faturamento total foi R${soma}')
    print(f'O fatura da loja B foi superado em R${diferença}')
else:
    print(f'Faturamento dos clientes foi {soma}. O faturamento da loja B não foi superado.')
