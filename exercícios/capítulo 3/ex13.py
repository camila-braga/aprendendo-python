print ('Digite uma medida em pés.')
medida = float(input())

pol = medida*12
jarda = medida/3
milha = jarda/1760

print ('A conversão em polegadas é {:.2f}'.format(pol))
print ('A conversão em jardas é {:.2f}'.format(jarda))
print ('A conversão em milha é {:.5f}'.format(milha))
