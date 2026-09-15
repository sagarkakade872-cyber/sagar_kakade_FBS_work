# Take input
X = int(input('Enter the value of x:'))
Y=int(input('Enter the value y:'))

#swapping
print(f'before swapping X:{X},Y:{Y}')

Z = Y
Y = X
X = Z
print(f'after swapping X:{X}, Y:{Y}')
