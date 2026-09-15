# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

Correct_userid="sagar"
Correct_Pass="Sagar8767"

for i in range(3):
    user_id=(input("enter your User id:"))
    pass_word=(input("enter your Password:"))
    if (user_id==Correct_userid and pass_word==Correct_Pass):
       print("login successfully")
       break
    else:
       print("invalid userid or password")
else:
   print("3 times to get chance login")       
