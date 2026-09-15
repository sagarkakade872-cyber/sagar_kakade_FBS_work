#WAP to print factorial of a number .


num = int(input("Enter number:"))
sum=1
for i in range (1,num+1):
    print(i)
    sum=sum*i

print("Sum of n factorial:",sum)
    