#Wap to print between 1 to 100
num=int(input("enter number:"))
for num in range(3,num+1):
    for i in range (2,num):
        if(num%i==0):
            break
    else:
        print(num)    