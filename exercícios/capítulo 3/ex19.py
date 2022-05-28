print('Qual altura do degrau, em metros?')
degrau = float(input())
print('Qual altura que se deseja alcançar subindo a escada, em metros?')
altura = float(input())

quantidade = altura/degrau

print('Quantidade de degraus a serem subidos = {:.1f}'.format(quantidade))
