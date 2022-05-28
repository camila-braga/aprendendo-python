print ('Qual é o salário?')
salario = float(input())

print ('Qual é o percentual de aumento?')
aumento = float(input())

aumento = salario*aumento/100

print ('O aumento será =', aumento)

salario = salario + aumento

print ('e o salário atualizado será =', salario)
