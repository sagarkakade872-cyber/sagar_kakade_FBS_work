#take 3 input
P= int(input("P is principle: "))
R= int(input("R is range: "))
T=int(input("T for time: "))

#calculation
Ci= P*(1+R/100)**T
print(Ci)
