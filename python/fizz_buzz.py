a=int(input("Enter the number you want to print in the series:"))
for i in range(1,a):
    if(i%3==0):
        print("FIZZ")
    if(i%5==0):
        print("BUZZ")
    if(i%15==0):
        print("FIZZBUZZ")
    else:# this is linked to only the last part of the if so it executes everytime
        print(i)