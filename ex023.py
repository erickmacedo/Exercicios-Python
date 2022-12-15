num = int(input('Insira um número: '))

print(f'Analisando o número {num} ...')

m = num // 1000
c = ((num % 1000) // 100)
d = ((num % 100) // 10)
u = num % 10

print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')