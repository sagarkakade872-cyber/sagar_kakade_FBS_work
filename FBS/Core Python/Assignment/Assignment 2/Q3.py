#take input
F= float(input('Enter feet:'))
I= float(input('enter inches:'))

#formula
Tc= (F*30.48)+(I*2.54)
M= Tc/100
print(f'centemeter is:{Tc}, meter is:{M}.')
