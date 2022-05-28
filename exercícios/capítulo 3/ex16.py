print('Digite o salário mínimo.')
salario = float(input())
print('Qual o número de horas trabalhadas?')
horas_trabalhadas = float(input())

umaHora = salario/2
bruto = horas_trabalhadas*umaHora
imposto = 0.03*bruto
salario = bruto - imposto

print('Salário a receber = {:.2f}'.format(salario))
