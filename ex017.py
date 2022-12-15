from math import hypot

x = float(input('Digite o cateto oposto: '))
y = float(input('Digite o cateto adjacente: '))

print(f'a hipotenusa vai medir {hypot(x,y):.2f}')