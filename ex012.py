price = float(input(f'Qual o preço do produto? R$'))
newprice =  price - (price * (5/100))
print(f'O produto que custava {price}, na promoção com desconto de 5% vai custar {newprice}')