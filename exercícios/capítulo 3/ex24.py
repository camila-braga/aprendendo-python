print('Digite a hora')
hora = float(input())

minutos = (hora - int(hora))*100

hora_min = int(hora)*60

total = hora_min + minutos

print('Total de minutos é', total)
