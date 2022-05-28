print('Digite o saldo médio.')
saldo = float(input())

if saldo <= 200:
    credito = 0.1*saldo
    print('Para saldo R${:.2f}'.format(saldo),'o crédito será de R${:.2f}'.format(credito))
elif saldo > 200 and saldo <= 300:
    credito = 0.2*saldo
    print('Para saldo R${:.2f}'.format(saldo),'o crédito será de R${:.2f}'.format(credito))
elif saldo > 300 and saldo <= 400:
    credito = 0.25*saldo
    print('Para saldo R${:.2f}'.format(saldo),'o crédito será de R${:.2f}'.format(credito))
elif saldo > 400:
    credito = 0.3*saldo
    print('Para saldo R${:.2f}'.format(saldo),'o crédito será de R${:.2f}'.format(credito))
