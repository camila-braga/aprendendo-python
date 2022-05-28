print ('Qual o salário mínimo?')
salario = float (input())
print ('Qual o número de horas trabalhadas?')
horas = float (input())
print ('Quantos dependentes tem o funcionário?')
dependentes = float (input())
print ('Quantas horas extras trabalhadas?')
extras = float (input())

salariomes = horas*salario*(1/5)
acrescimodep = 32*dependentes
extratot = extras*(salario/5 + 0.5*salario/5)
bruto = salariomes + acrescimodep + extratot

if bruto < 200:
    imposto = 0
else:
    if 200 <= bruto and bruto<= 500:
        imposto = 0.1*bruto
    else:
        imposto = 0.2*bruto

liquido = bruto - imposto

if liquido <= 350:
    gratificacao = 100
else:
    gratificacao = 50

salariofinal = liquido + gratificacao
print('O salário final a receber será', salariofinal)
