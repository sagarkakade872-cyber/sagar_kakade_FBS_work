amount=int(input('Enter the amount:' ))


n500= amount//500
amount= amount%500

n200= amount//200
amount= amount%200

n100= amount//100
amount= amount%100

n50= amount//50
amount= amount%50

n20= amount//20
amount= amount%20

n10=amount//10
amount= amount%10

n5= amount//5
amount=amount%5

n2= amount//2
amount= amount%2


print('500 notes:',n500)
print('200 notes:',n200)
print('100 notes:',n100)
print('50 note:',n50)
print('20 notes:',n20)
print('10 notes:',n10)
print('5 rupees:',n5)
print('2 rupees:', n2)


