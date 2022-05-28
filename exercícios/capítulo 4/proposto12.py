print('Qual o salário bruto do funcionário?')
bruto = float(input())
imposto = bruto*0.07

if bruto <= 350:
    grat = 100
    salario = bruto + grat - imposto
    print('Salário a receber será de R${:.2f}'.format(salario))

elif bruto > 350 and bruto < 600:
    grat = 75
    salario = bruto + grat - imposto
    print('Salário a receber será de R${:.2f}'.format(salario))

elif bruto >= 600 and bruto <= 900:
    grat = 50
    salario = bruto + grat - imposto
    print('Salário a receber será de R${:.2f}'.format(salario))

elif bruto > 900:
    grat = 35
    salario = bruto + grat - imposto
    print('Salário a receber será de R${:.2f}'.format(salario))
