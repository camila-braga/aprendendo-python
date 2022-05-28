print ('Digite a primeira nota e seu peso.')
n1 = float(input())
p1 = int(input())

print ('Digite a segunda nota e seu peso.')
n2 = float(input())
p2 = int(input())

print ('Digite a terceira nota e seu peso.')
n3 = float(input())
p3 = int(input())

media = (n1*p1 + n2*p2 + n3*p3)/(p1 + p2 + p3)

print ('A média ponderada será =', media)
