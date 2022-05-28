print('Digite 3 números')
n1 = float(input())
n2 = float(input())
n3 = float(input())

if n1<n2 and n1<n3:
    print(n1)
else:
    if n3<n1 and n3<n2:
        print(n3)
    else:
        print(n2)
    
