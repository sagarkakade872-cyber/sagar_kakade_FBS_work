num = int(input("Enter number:"))
for i in range(2,num):
    if(num%i==0):
       print(f'{num} is not a prime number')
       break
else:
     print(f'{num} is a prime number')

    # code
# X= int(input('Enter first number:'))
# y= int(input("enter last number"))

# for i in range(X, y +1):
#     if(i==0):
#      print(f" The number is not prime")
#      break
# else:
#    print(f'the number is prime')    


