#WAP to print sum of series upto n.

num = int(input("Enter number:"))
sum=0
for i in range (1,num+1):
    print(i)
    sum=sum+i

print("Sum of n series:",sum)
    