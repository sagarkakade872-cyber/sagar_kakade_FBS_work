#Write a program to print first n prime number
n= int(input("Enter the number"))

num=2
while n>0:
    for i in range (2,num):
        if num%i==0:
            break
    else:
        print(num)    
        n-=1
    num+=1
        