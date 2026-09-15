#Input 5 subject marks from user and display grade(eg.First class,Second class 
s1=int(input("Enter math marks:"))
s2=int(input("enter chemistry marks:"))
s3=int(input("Enter english marks:"))
s4=int(input("Enter physics marks:"))
s5=int(input("Enter biology marks:"))

sum = s1+s2+s3+s4+s5

grade=sum/5
if(grade>=80):
    print("first class")
elif(grade>=60):
    print("second class")
else:
    print("fail")
