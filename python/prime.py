def prime(number):
    li=list(range(1,number))
    count=0
    for i in li:
        if(number%i==0):
            count+=1
    else:
        if(count==1):
            print("The number you enterd is a prime")
        else:
            print("The number you enterd is not a prime")

n=input("Enter a number to check whether it is prime or not:")
num=int(n)
prime(number=num)