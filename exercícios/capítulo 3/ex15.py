print('Qual o preço de fábrica?')
fabrica = float(input())
print('Qual o percentual de lucro do distribuidor?')
perc_lucro = float(input())
print('Qual o percentual de impostos?')
perc_imposto = float(input())

preco_lucro = fabrica*perc_lucro/100
preco_imposto = fabrica*perc_imposto/100
preco_final = fabrica + preco_lucro + preco_imposto

print('Valor correspondente ao lucro do distribuidor = {:.2f}'.format(preco_lucro))
print('Valor correspondente aos impostos = {:.2f}'.format(preco_imposto))
print('Preço final do veículo = {:.2f}'.format(preco_final))
