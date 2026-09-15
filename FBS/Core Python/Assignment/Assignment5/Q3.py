# 3. Accept no. of passengers from user and per ticket cost. Then accept age of eachpassenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
ticket=int(input('enter the price of ticket:'))

total=0

for i in range(5):
    age=int(input('enter the age:'))
    if(age<12):
        discount=ticket*30/100
        ticket=ticket-discount
        print(ticket)
        total=total+ticket
    elif(age>59):
        discount=ticket*50/100
        ticket=ticket-discount
        print(ticket)
        total=total+ticket

    else:
        print(ticket)
        total=total+ticket


print(total)