# Write a program to check if entered number is a palindrome or
# not.

def palindrome():
    n=int(input("enter the number:"))
    reverse=0
    temp=n
    while(temp>0):
        d=temp%10
        reverse=reverse*10+d
        temp=temp//10
    if (reverse==n):
        return True
    else:
        return False
res=palindrome()
print(res)    

    