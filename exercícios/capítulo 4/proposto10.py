print ('Qual o custo de fábrica?')
custo = float(input())

dist = 0.05*custo
imposto = 0

if custo > 12000 and custo <= 25000:
    dist = 0.1*custo
    imposto = 0.15*custo
elif custo > 25000:
    dist = 0.15*custo
    imposto = 0.30*custo

custo = custo + dist + imposto
print('Preço será de R${:.2f}'.format(custo))

'''
if custo <= 12000:
    dist = 0.05*custo
    imposto = 0
    custo = custo + dist + imposto
    print('Preço será de R${:.2f}'.format(custo))

else:
    if custo > 12000 and custo <= 25000:
        dist = 0.1*custo
        imposto = 0.15*custo
        custo = custo + dist + imposto
        print('Preço será de R${:.2f}'.format(custo))

    elif custo > 25000:    
        dist = 0.15*custo
        imposto = 0.2*custo
        custo = custo + dist + imposto
        print('Preço será de R${:.2f}'.format(custo))
    
'''