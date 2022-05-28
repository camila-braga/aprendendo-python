print('Qual o salário?')
salario = float(input())
print('Quantidade de quilowatt consumida:')
quantidade = float(input())

quilowatt = salario/5
print('O valor do quilowatt = {:.2f}'.format(quilowatt))

residencia = quilowatt*quantidade
print('Valor a ser pago = {:.2f}'.format(residencia))

desconto = residencia - residencia*0.15
print('Valor a ser pago com desconto = {:.2f}'.format(desconto))

