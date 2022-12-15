nome = str(input('Digite seu nome completo: '))

print('Analisando o seu nome...')

print(f'O seu nome em maíusculas é {nome.upper()}')
print(f'O seu nome em minusculas é {nome.lower()}')

count_name = nome.replace(' ', '')
print(f'O seu nome ao todo tem {len(count_name)}')

print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras')
