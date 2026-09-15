# WAP to print Fibonacci series upto n.
num=int(input("Enter number:"))
a=-1
b=1
temp=num
for i in range(1,num+1):
    c=a+b
    print(c)
    a=b
    b=c
