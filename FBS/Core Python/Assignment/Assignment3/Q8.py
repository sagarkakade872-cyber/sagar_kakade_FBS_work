#Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)
import random
userid=input("enter userid:")
password=input("enter password:")
if(userid=="Sagarkakade" and password=="sagar8767"):
    systemcap=random.randint(1000,10000)
    print(systemcap)
    capture=int(input("enter the number"))
    if(systemcap==capture):
        print(f'login successfully')
    else:
        print("invalid capture")
else:
    print("invalid pass and user id" )         
    