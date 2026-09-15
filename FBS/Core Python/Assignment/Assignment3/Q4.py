#Write a program to input all sides of a triangle and check whether triangle is valid or not 
A=int(input("Enter triangle a:" ))
B=int(input('enter triangle b:'))
C=int(input('Enter traingle c:'))

if(A+B>C and B+C>A and C+A>B):
    print(f'the traingle is valid')
else:
    print(f'the traingle is not valid')    