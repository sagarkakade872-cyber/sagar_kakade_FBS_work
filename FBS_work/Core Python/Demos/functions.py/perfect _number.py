# def perfect():
#     num=int(input('enter the number:'))
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#           sum=sum+i

#     if(sum==num):
#                print("true")
#     else:
#         print("false")        

# perfect()
                        
                         # type2

# def perfect(num):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#           sum=sum+i

#     if(sum==num):
#                print("true")
#     else:
#         print("false")        
# num=int(input('enter the number:'))

# perfect(num)

                        #type3


# def perfect():
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#           sum=sum+i

#     if(sum==num):
#                return ("true")
#     else:
#         return ("false")        
# num=int(input('enter the number:'))
# res=perfect()
# print(res)


                        #type 4
def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
          sum=sum+i

    if(sum==num):
               return ("true")
    else:
        return ("false")        
num=int(input('enter the number:'))
res=perfect(num)
print(res)
