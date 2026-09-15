# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

def Armstrong(n):
    sum=0
    temp=n

    while temp>0:
        d=temp%10
        sum=sum+d**3
        temp=temp//10
        
    if(n==sum):
        return True
    else:
        return False
    
n=int(input("enter the number:"))

res=Armstrong(n)
print(res)


