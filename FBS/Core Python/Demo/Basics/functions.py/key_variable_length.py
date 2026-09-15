#1 To pass multiple parameter with meaning
#use 2 (**) asterisk symbol before parameter function defintion 
#3 passed data will be store in dictionary format
#4 use for loop to iterate value in dict.items()

def emp(**data):
    for key, val in data.items():
        print(key,":",val)  
emp(id=101, dep="IT",sal=20000, name="Sagar")        