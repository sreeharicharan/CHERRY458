lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
for a in range (lower,upper+1):
    if(a%7==0 and a%5==0):
        print(a)
