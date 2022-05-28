

print('Digite um número real')
nreal = float(input())
parteinteira = int(nreal)
print('Parte inteira é ', parteinteira)
partefrac = float(nreal-parteinteira)
print('Parte fracionária é {0:016.2f} ---- {1:4d}'.format(partefrac, int(nreal)))
if partefrac < 0.5:
    print('Número arredondado é ', int(nreal))
else:
    print('Número arredondado é ', int(nreal) + 1)



