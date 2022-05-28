print('Quais as duas dimensões do cômodo?')
dim1 = float(input())
dim2 = float(input())

area = dim1*dim2
print('A área do cômodo é {:.2f}'.format(area))

pot = area*18
print('A potência necessária é de', round(pot),'W.')
