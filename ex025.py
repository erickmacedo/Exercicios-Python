name = str(input('Qual seu nome completo? '))

name = name.strip().title()

check = 'Silva' in name

print(f'Seu nome tem Silva? {check}')