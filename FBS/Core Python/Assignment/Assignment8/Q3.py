
# 3. Write a program to find sum of following series using functions


# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

# def a(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     return sum
# n=int(input("enter number:"))
# res=a(n)    
# print(res)


                        # b. 1!+ 2! + 3! + 4!+..... + n!

# def b():
#     sum=0
#     fact=1
#     for i in range (1,n+1):
#         fact=fact*i
#         sum=sum+fact
#     return sum
# n=int(input("enter number:"))
# res=b()
# print(res)

                    # c. 1^1 + 2^2 + 3^3+ ...... n^n
def C():
    sum=0
    for i in range(1,n+1):
        sum=sum+i**i
    return sum
n=int(input("enter number:"))
res=C()
print(res)