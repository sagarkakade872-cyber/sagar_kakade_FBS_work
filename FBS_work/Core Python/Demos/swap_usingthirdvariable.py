x=10
y=20

print(f'Before swapping x:{x}, y:{y}.')

x,y = y,x

y = x
z = y
x = z 

print(f'After swapping x:{x}, y:{y}.')
