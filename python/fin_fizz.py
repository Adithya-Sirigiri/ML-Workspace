a=int(input("Enter the number you want to print in the series:"))
for i in range(1,a):
    if(i%15==0):
        print("FIZZBUZZ")
    elif(i%3==0):
        print("FIZZ")
    elif(i%5==0):
        print("BUZZ")
    else:
        print(i)
    