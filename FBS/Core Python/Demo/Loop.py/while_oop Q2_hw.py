# i = 1
# while(i<=10):
#     print(i)
#     i+=1

#2.
# num= int(input('enter the number:'))

# i = 1
# while i <= 10:
#     print(num, "x", i, "=", num * i)
#     i += 1

#3 seperate number
# num= 345
# while(num>0):
#     d=num%10
#     print(d)
#     num=num//10

#4. sum of number using while loop 

num= 472

sum=0
while(num>0):
    d=num%10
    sum+=d
    num=num//10
print(sum)