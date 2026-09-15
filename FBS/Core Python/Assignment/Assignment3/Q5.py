#Write a program to check whether the triangle is equilateral, isosceles or scalene traingle 
A= int(input("Enter the the Angle1:"))
B= int(input("Enter the angle 2:"))
C= int(input("Enter the angle 3 :"))
if(A==B and B==A and C==A):
    print(f'the angle is equilateral')
elif(A==B or B==A or C==A):
    print(f'its is isosceles')
else:
    print(f'It is scalene traingle')    