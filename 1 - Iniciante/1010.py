x1,y1,z1 = map(float, input().split(' '))
x2,y2,z2 = map(float, input().split(' '))

valor_total = (y1*z1) + (y2*z2)

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')