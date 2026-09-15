#                       #type 1
# def strong():
#     num=int(input("Enter number:"))
#     sum=0
#     temp=num
#     while (temp>0):
#         d=temp%10
#         temp=temp//10
#         fact=1
#     for i in range (1,num+1):
#         fact=fact*i

#     sum= fact+sum
#     temp=temp//10

#     if(fact==sum):
#         print("true")    
#     else:
#         print(False)
# strong()        

                   #type 2

# def strong(num):
#     n = num
#     sum=0
#     temp=n
#     while(n>0):
#         d= temp%10
        
#         fact=1
#         for i in range (1,d+1):
#             fact = fact * i

#         sum= fact+sum
#         n = n // 10

#     if(sum==num):
#         print("true")    
#     else:
#         print("false")
# num=int(input("enter number:"))        
# strong(num) 


                              #3
# def strong():
#     num=int(input("enter number:"))
#     sum=0
#     temp=num
    
#     while(temp>0):
#         d=temp%10
#         fact=1
#         for i in range(1,d+1):
#             fact=fact*i
#          sum=fact+sum
#          temp=temp//10
#     if(sum==num):
#         return "true"
#     else:
#         return "false"
# res=strong()
# print(res) 
            
                       #type 4

def strong(n):
    sum=0
    temp=num
    while(temp>0):
        d= temp%10
    
        fact=1
    for i in range (1,d+1):
        fact=fact*i
        sum=fact+sum
        temp=temp//10
    if (sum==num):
        return "true"
    else:
        return "false"
num=int(input("enter number:"))
res=strong("n")    
print(res)