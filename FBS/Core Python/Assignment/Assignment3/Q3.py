#Write a program to input angles of a triangle and check whether triangle is valid or not. 

A1= int(input("Enter angle 1:"))
A2=int(input("Enter angle 2:"))
A3= int(input("enter the angle 3:"))
sum = A1+A2+A3

if (sum<=180):
    print(f'The angle is valid')
else:
    print(f'the traingle is not valid')    

          