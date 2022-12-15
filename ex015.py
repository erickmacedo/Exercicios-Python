days = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

total = (days * 60) + (km * 0.15)

print(f'O total a pagar é R${total}')
