# Write a program find reverse of a number


def rev(n):
      reverse=0
      temp=n
      while(temp>0):
            d=temp%10
            reverse=reverse*10+d
            temp=temp//10
      return("rev=", reverse)
      
n=int(input("enter number:"))
res=rev(n)
print(res)