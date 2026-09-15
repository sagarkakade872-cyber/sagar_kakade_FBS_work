# 4. WAP to print Armstrong number within a given range
num=int(input('Enter number'))
temp=num
count=0
for i in range(1,num+1):
    sum=0
    temp=i
    while(temp>0):
        digit=temp%10
        sum+=digit**3
        temp//=10
    if sum==i:
      print(i)    
        



