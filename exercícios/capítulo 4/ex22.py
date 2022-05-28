print ('Digite o salário.')
salario = float(input())
print ('Digite o tempo de serviço, em anos.')
tempo = float(input())

print('O imposto será:')
if salario<200:
    imposto = 0
else:
    if  salario>=200 and salario <=450:
        imposto = 0.03*salario
    else:
        if 450 < salario and salario < 700:
            imposto = 0.08*salario
        else:
            imposto = 0.12*salario
print (imposto)

print('A gratificação será:')
if salario> 500:
    if tempo <=3:
        gratificacao = 20
    else:
        gratificacão = 30
else:
    if tempo <=3:
        gratificacão = 23
    else:
        if 3 < tempo and tempo < 6:
            gratificacao = 35
        else:
            gratificacao = 33
print (gratificacao)

salario = salario - imposto + gratificacao
print ('O salário líquido será', salario)

print('A categoria será:')
if salario <= 350:
    print ('A')
else:
    if 350 < salario and salario< 600:
        print ('B')
    else:
        print('C')



    

        
