print ('Digite o salário mínimo')
salario = float(input())
print ('Digite o turno: M, V ou N')
turno = str(input())
print ('Digite a categoria: O ou G')
categ = str(input())
print ('Digite o número de horas trabalhadas no mês')
horas = float(input())

print('Cálculo do coeficiente do salário:')
if turno == 'M':
    coef = 0.1*salario
else:
    if turno == 'V':
        coef = 0.15*salario
    else:
        if turno == 'N':
            coef = 0.12*salario
        else:
            print('Não é possível calcular devido ao turno ser inválido')
print (coef)

bruto = coef*horas
print('O salário bruto é', bruto)

print('Cálculo do imposto:')
if categ == 'O':
    if bruto < 300:
        imposto = 0.03*bruto
    else:
        imposto = 0.05*bruto
else:
    if categ == 'G':
        if bruto < 400:
            imposto = 0.04*bruto
        else:
            imposto = 0.06* bruto
    else:
        print('Não e possível calcular devido à categoria ser inválida')
print(imposto)

print ('Cálculo da gratificação:')
if turno == 'N' and horas > 80:
    gratificacao = 50
else:
    gratificacao = 30
print (gratificacao)

print('Cálculo do auxílio alimentação:')
if categ == 'O' or coef <=25:
    aux = bruto/3
else:
    aux = bruto/2
print (aux)

liquido = bruto - imposto + gratificacao + aux
print('O salário líquido será', liquido)

print('A classificação é')
if liquido < 350:
    print('Mal remunerado')
else:
    if 350 <= liquido and liquido <= 600:
        print('Normal')
    else:
        print('Bem remunerado')

        
        



    
