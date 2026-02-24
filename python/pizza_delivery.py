#Example of mltiple if's
na=input("Do you want Adithya then enter Y/y for yes:")
bill=0
if (na=="Y" or na=="y"):# see here for characters you have to use double quotes and also the assignment operators correctly
    name=int(input("Enter the type of Adithya from the options:\n 1.Small \n2.Medium \n3.Large:\n"))
    if(name==1):
        print("The small Adithya is 100/-")
        bill+=100
    elif(name==2):
        print("The medium Adithya is 200/-")
        bill+=200
    else:
        print("The large Adithya is 300/-")
        bill+=300
    
    choice=input("Do you want macroni\n Enter Y/y for yes:")
    if(choice=="y" or choice=="Y"):
        chow="Enter 1 for small Adithya and 2 for large Adithya:"
        if(chow==1):
            print("You have to pay 30/-")
            bill+=30
        else:
            print("You have to pay 50/-")
            bill+=50
    fu=input("Enter Y or y for cheese on any Adithya:")
    if(fu=="y" or fu=="Y"):
        print("You have to pay 20/-")
        bill+=20

    total_bill=bill #everything should follow the same idendation while writing
    print(f"The total bill is:{total_bill}")

else:
    print("They do not want Adithya")

print("Bye!")