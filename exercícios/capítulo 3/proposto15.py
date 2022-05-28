print('Digite o salário')
salario = float(input())
print('Digite os valores das duas contas a serem pagas.')
conta1 = float(input())
conta2 = float(input())

multa1 = conta1 + conta1*0.02
multa2 = conta2 + conta2*0.02

salario = salario - multa1 - multa2
print('O valor restante do salário é {:.2f}'.format(salario))
