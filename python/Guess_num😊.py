print("Let me think of a number between 1 to 50")
var=input("Choose level of dificulty...Select easy(10 attempts) or hard(5 attempts):")
num=40
if(var=="easy"):
    print("You have 10 attempts remaining to guess the number:")
    j=10
    for i in range(10):
        guess=int(input("Make a guess:"))
        if(guess==num):
            print("You guessed it right....")
            break
        elif(guess<num and guess>=(num-5)):
            print(f"Your guess is close\nGuess Again\n You have {j-1} attempts to guess the number")
        elif(guess<(num-5) and guess>=(num-15)):
            print(f"Your guess is too low and aim for higher\n Guess Again \n You have {j-1} attempts to guess the number")
        elif(guess<(num-15)):
            print(f"Out of range and AIM for higher!!!\n Guess Again \n You have {j-1} attempts to guess the number")
        elif(guess>num and guess<=(num+5)):
            print(f"Your guess is close \n Guess Again \n You have {j-1} attempts to guess the number")
        elif(guess>(num+5) and guess<=(num+15)):
            print(f"Your guess is too high and aim for lower \n Guess Again \n You have {j-1} attempts to guess the number")
        elif(guess>(num+15)):
            print(f"Out of range and AIM for lesser!!! \n Guess Again \n You have {j-1} attempts to guess the number")
        j=j-1

