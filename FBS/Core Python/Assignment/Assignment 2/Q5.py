# Take input
Cost_price = int(input('enter cost price is:'))
Dis_price = int(input('Enter discount price is:'))

#formula
Dis_amount = (Cost_price*Dis_price)/100
Selling_price = Cost_price - Dis_price

print(f'discount amount is:{Dis_amount}:')
print(f'selling price is {Selling_price}:')