print('Qual o custo?')
custo = float(input())
print('Qual o preço do convite?')
convite = float(input())

quantidade = custo/convite

print('Devem ser vendidos no mínimo', int(quantidade),'convites.')
