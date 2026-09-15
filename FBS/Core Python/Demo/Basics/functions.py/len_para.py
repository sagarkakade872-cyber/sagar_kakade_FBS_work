#1 pass multiple parameter in function 
#2 mention asterisk (*) symbol before parameter in function  definition 
#3 value store tuple format
#4 use for loop to iterate value from tuple 



def addition(*num):
    sum=0
    for val in num:
        sum+=val
    return sum 

res=addition(10,20,30,40,50)
print(res)        

