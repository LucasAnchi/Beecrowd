nome = str(input())
sal_fixo = float(input())
total_vendas = float(input())

total = sal_fixo + (15/100*total_vendas)

print(f'TOTAL = R$ {total:.2f}')