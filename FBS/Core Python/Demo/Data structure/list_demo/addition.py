li=[10,20,30,40,50,60,70]

sum=0 

#Method 1 iterating values 
# for ele in li:
#   Sum+=ele

#Method 2:
for ind in range(0,len(li)):
    sum+=li[ind]
print(sum)    