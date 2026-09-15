num= int(input("Enter the number:"))
temp=num
rev_num = num
while(num>0):
    d= temp%10
    temp=temp//10
    rev_num= rev_num*10+d
    if(rev_num==num):
        print("the number is palindrome.")
    else:
        print("the number is not palindrome.")    