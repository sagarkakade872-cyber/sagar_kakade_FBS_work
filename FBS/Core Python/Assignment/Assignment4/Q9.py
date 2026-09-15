# 9. WAP to print all numbers in a range divisible by a given number.

n1=int(input("Enter start number:"))
n2= int(input("Emter end number:"))
num=int(input("enter number divide by:"))
for i in range(n1, n2+1):
    if(i%num==0):
        print(i)
