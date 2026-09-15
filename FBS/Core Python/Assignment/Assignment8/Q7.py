# 7. Write a program to find sum of digits of a number.

def sum():
    sum=0
    num=int(input("enter num: "))
    while(num>0):
        d=num%10
        sum=sum+d
        num=num//10
    print("sum of digit=",sum)
sum()        