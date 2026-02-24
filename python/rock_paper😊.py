#Order is very important in this code
import random
user_choice=int(input("enter a number if\n0 for ROCK\n1 for PAPER\n2 for scissors:\n"))
computer_choice=random.randint(0,2)
if(computer_choice==user_choice):
    print(f"It is draw and the computer choice is:{computer_choice}")
if(user_choice==0 and computer_choice==2):#these should be written first
    print(f"You win and the computer choice is:{computer_choice}")
if(user_choice==2 and computer_choice==0):#these should be written first
    print(f"You lose and the computer choice is:{computer_choice}")
elif(computer_choice>user_choice):#if user enters 0 and computer choice is 2 then this statements will execute first and will give false result
    print(f"You lose and the computer choice is:{computer_choice}")
elif(user_choice>computer_choice):
    print(f"You win and the computer choice is:{computer_choice}")