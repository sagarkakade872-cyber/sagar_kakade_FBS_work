def prime(num):
    flag= True
    if (num % 2==0):
        flag = False

    return flag
num=int(int(input("enter number:")))
res=prime(num)
print(res)
