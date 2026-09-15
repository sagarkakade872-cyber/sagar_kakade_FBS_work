gender = input('Enter your gender (M/F):')

age = int(input('Enter your age:'))

if (gender=='F'):
    if(age>=18):
        print('Girl is eligible For marriage')
    else:
         print('pehele padhai kar lo')
else:
    if(age>=20):
        print('boy is eligible for marriage.')
    else:
        print('pehele kama lo.')


