print ('Qual o preço?')
preco = float(input())
print ('Qual o tipo? A, L ou V')
tipo = str(input())
print ('Produto necessita de refrigeração? S para sim, N para não.')
refr = str(input())

if refr =='N':
    if tipo =='A':
        if preco < 15:
            add = 2
        else:
            add = 5
    else:
        if tipo =='L':
            if preco < 10:
                add = 1.5
            else:
                add = 2.5
        else:
            if tipo =='V':
                if preco < 30:
                    add = 3
                else:
                    add = 2.5
else:
    if refr == 'S':
        if tipo =='A':
            add = 8
        else:
            if tipo =='L':
                add = 0
            else:
                if tipo == 'V':
                    add =0
print('O valor adicional =', add)
            
if preco < 25:
    imposto = 0.05*preco
else:
    imposto = 0.08*preco
print('O valor do imposto =',imposto)

custo = preco + imposto
print('O preço de custo =', custo)

if tipo =='A' or refr =='S':
    desconto = 0
else:
    desconto = 0.03*custo
print('Desconto =', desconto)

preco = custo + add - desconto
print('Novo preço =', preco)

if preco <= 50:
    print('Barato')
else:
    if 50 < preco and preco < 100:
        print('Normal')
    else:
        print('Caro')

        
