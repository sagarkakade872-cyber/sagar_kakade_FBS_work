#1. pass: Neglect expect indendation error 

for i in range(1,10):
    pass 

#2 break: for terminating the loop
for i in range(1,10):
    if(i==4):
        break
    print(i)

#3. continue: to stop particular iteration
for i in range(1,10):
    if(i==4):
        continue
    print(i)

#4 else : will executed when loop is excecuted successfully
for i in range (1,10):
    if(i==4):
        break
    print(i)
else:
    print('else block is executed')    