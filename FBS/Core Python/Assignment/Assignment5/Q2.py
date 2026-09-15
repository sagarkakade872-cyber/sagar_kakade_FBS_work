# Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n= int(input("enter students:"))
Total_percentage= 0
for i in range (1, n+1):
    print("enter marks students", i)
    m1=float(input("enter subjects 1 marks:"))
    m2=float(input("enter subject 2:"))
    m3=float(input("enter subject 3:"))
    m4=float(input("enter subject 4:"))
    m5= float(input('enter subject 5:'))
Total= m1+m2+m3+m4+m5
percentage=(Total/500)*100
print("percentage of student",i,"=",percentage,"%")
Total_percentage+=percentage
average=Total_percentage/n
print("average percentage=",average,"%")