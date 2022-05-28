print ('Qual o preço atual do produto?')
precoatual = float(input())
print ('Qual a venda média mensal desse produto?')
vendamedmensal = float(input())

if precoatual < 30 or vendamedmensal < 500:
    novopreco = precoatual + 0.1*precoatual
else:
    if 30>= precoatual and precoatual<80 or 500>= vendamedmensal and vendamedmensal<1200:
        novopreco = precoatual + 0.15*precoatual
    else:
        novopreco = precoatual - 0.20*precoatual

print ('Preço atualizado =', novopreco)

        
