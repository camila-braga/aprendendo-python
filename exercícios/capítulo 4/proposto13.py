print('Qual o preço do produto?')
preco = float(input())

if preco <= 50:
    preco = preco + 0.05*preco
    print ('Novo preço é de R${:.2f}'.format(preco),'.')
elif preco > 50 and preco <=100:
    preco = preco + 0.1*preco
    print ('Novo preço é de R${:.2f}'.format(preco),'.')
elif preco > 100:
    preco = preco + 0.15*preco
    print ('Novo preço é de R${:.2f}'.format(preco),'.')

if preco <= 80:
    print('Barato.')
elif preco > 80 and preco <= 120:
    print('Normal.')
elif preco > 120 and preco <= 200:
    print('Caro.')
elif preco > 200:
    print('Muito caro.')
