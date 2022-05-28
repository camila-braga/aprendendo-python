print('Digite o valor do salário.')
salario = float(input())

if salario >= 500:
    print('Não tem direito ao aumento.')
else:
    salario = salario + 0.3*salario
    print('Salário reajustado = {:.2f}'.format(salario))
    
