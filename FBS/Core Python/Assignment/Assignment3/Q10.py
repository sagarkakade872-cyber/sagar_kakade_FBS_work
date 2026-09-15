# 10. Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

gender = (input("enter gender M/F:"))
age= int(input("enter your age:"))

if(gender=='F'):
    if(age>=18):
          print("Girl is eligible for marriage")
            
    else:
         print('pehle padhai kar')
else:
     if(gender=='M'):
          if(age>=21):
               print(" boy is elgible for marrage")
          else:
               print('pehele kama loo')
          
