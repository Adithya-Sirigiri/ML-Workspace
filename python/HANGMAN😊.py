#in hangman the length of the digit can be anything but we are given only 6 attempts to compltet the game 
name=['p','a','r','i','s']
name[0]="p"
name[1]="a"
name[2]="r"
name[3]="i"
name[4]="s"
count=0
print("Lets play Hangman!!\nYou have only 6 lives so try guess the word within 6 attempts!GOOD LUCK!!")
guess=['_','_','_','_','_']
print(guess)
for i in range(0,6):
    es=input("Guess a letter:")
    #guess[i]=es here we are assigning guess[0] as a initially so we are causing and error
    if(es==name[0]):
        guess[0]="p"
        print(guess)
    elif(es==name[1]):
        guess[1]="a"
        print(guess)
    elif(es==name[2]):
        guess[2]="r"
        print(guess)
    elif(es==name[3]):
        guess[3]="i"
        print(guess)
    elif(es==name[4]):
        guess[4]="s"
        print(guess)
    else:
        print(f"You guessed \"{es}\" that is not present in the word so you lose a life")
        count+=1
        if(count==1):
            print("- - - - - - - - - - - \n   |             |\n   O             |\n                 |\n                 |\n                 |\n                 |\n---------------------\n---------------------")
        elif(count==2):
            print("- - - - - - - - - - - \n   |             |\n   O             |\n   |             |\n                 |\n                 |\n                 |\n---------------------\n---------------------") 
        elif(count==3):
            print("- - - - - - - - - - - \n   |             |\n   O             |\n  /|             |\n                 |\n                 |\n                 |\n---------------------\n---------------------")
        elif(count==4):
            print("- - - - - - - - - - - \n   |             |\n   O             |\n  /|\\           |\n                 |\n                 |\n                 |\n---------------------\n---------------------")
        elif(count==5):
            print("- - - - - - - - - - - \n   |             |\n   O             |\n  /|             |\n                 |\n                 |\n                 |\n---------------------\n---------------------")
        elif(count==6):
            print("- - - - - - - - - - - \n   |             |\n   O             |\n  /|\\           |\n                 |\n                 |\n                 |\n---------------------\n---------------------")
    