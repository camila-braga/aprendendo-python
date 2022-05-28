print('Qual o peso do saco de ração, em quilo?')
sacokg = float(input())

sacog = sacokg*1000

print('Qual a quantidade de ração fornecida, em gramas, para o primeiro gato?')
racao1_g = float(input())

print('Qual a quantidade de ração fornecida, em gramas, para o segundo gato?')
racao2_g = float(input())

racaodiaria = racao1_g + racao2_g
dia5emG = sacog - 5*racaodiaria
dia5emKG = dia5emG/1000

print('Em 5 dias, restarão {:.2f}'.format(dia5emG),'g ou {:.2f}'.format(dia5emKG),'kg.')
