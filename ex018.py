import math

x = float(input('Digite o angulo que você deseja: '))

print(f'O angulo de {x} tem o SENO de {math.sin(math.radians(x)):.2f}\nO angulo de {x} tem o COSENO DE {math.cos(math.radians(x)):.2f}')
print(f'O angulo de {x} tem a TANGENTE de {math.tan(math.radians(x)):.2f}')