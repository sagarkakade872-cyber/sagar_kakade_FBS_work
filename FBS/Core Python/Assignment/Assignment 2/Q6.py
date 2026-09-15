#Take input
Basic = int (input ('Enter Basic Salary:'))

#formula
DA = (10/100)* Basic
TA = (12/100)*Basic
HRA = (15/100)*Basic

#Display result
Total_salary = Basic + DA + TA + HRA
print("DA:", DA)
print("TA:", TA)
print("HRA:", HRA)
print(f'employee total salary:{Total_salary}') 