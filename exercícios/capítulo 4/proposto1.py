print('Digite as 4 notas do aluno.')
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

med = (nota1 + nota2 + nota3 + nota4)/4

if med >= 7:
    print('Aprovado')
else:
    print('Reprovado')
    
