print('Digite seu ano de nascimento e o ano atual')
nasc = int(input())
atual = int(input())

anos = atual - nasc
print('A idade em anos é',anos)

meses = anos*12
print('A idade em meses é',meses)

dias = meses*30.4
print('A idade em dias é',dias)

semanas = meses*4
print('A idade em semanas é',semanas)
