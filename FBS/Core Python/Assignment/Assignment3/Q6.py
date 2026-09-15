#Write a program to calculate profit or loss.
sp =int(input("enter price SP:"))
cp= int(input('Enter price cp:'))
profit=sp-cp
if(sp>cp):
    print(f'profit')
elif(cp>sp):
    print(f'loss')
else:
    cp==sp
    print(f'no profit no loss')    
   
