#1. to make parameter optional
#2. Assign value in parameter in function definition
#3. If we pass value to default para it take passed value 
#if we don't pass value to default para, it takes default value 
#4 flow from right to left (Why - positional parameter concept)

def emp(id,name,sal ,dept):
    print('ID:',id)
    
    print("Name:", name)
    print("Salary:", sal)
    print("DEPT:", dept)
emp(101,"xyz", 200000,"IT")    
print('##########')

