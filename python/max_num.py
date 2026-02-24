numbers=input("Please enter numbers to find the maximum with commas:")
number=numbers.split(",")
max=int(number[0])
for i in number:
    if(int(i)>max):
        max=int(i)
else:
    print("The max number is:",max)

    #correct code  -Adithya