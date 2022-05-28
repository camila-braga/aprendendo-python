print('Qual o salário e o valor das vendas?')
salario = float(input())
vendas = float(input())

comissao = 0.04*vendas
salario = salario + comissao
print('A comissão será de',comissao,'e o salário atualizado será de',salario)
