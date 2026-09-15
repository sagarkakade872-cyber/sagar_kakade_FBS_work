num=int(input("enter number:"))
sum=0
fact=1
for i in range(1,num+1):
    fact=fact*i
    sum=sum+fact
print("Sum of series:",sum)    
