#dice roll game
'''import random
while(True):
    roll=input("Roll the dice?(y/n:)").lower()
    if(roll=="n"):
        print("thanku for playing")
        break
    elif(roll!="y" and roll!="n"):
        print("invalid choice")
        break
    else:
        num1=random.randint(1,6)
        num2=random.randint(1,6)
        print(f"({num1},{num2})")'''
        
#guess the number
'''import random
number_to_guess=random.randint(1,100)
while(True):
    try:
        number=int(input("guess the number between 1 and 100:"))
        if(number_to_guess<number):
            print("too high ")
        elif(number_to_guess>number):
            print("too low")
        elif((number)==number_to_guess):
            print("conrats you guessed the number🏆")
            break
        else:
            print("enter a valid number")
    except ValueError:
        print("enter a number not a string")'''
#rock_paper_scissor
import random

choices=("p","r","s")
computer_choice=random.choice(choices)
emojis={"r":"🪨","s":"✂️","p":"📃"}

while(True):
   
    user_choice=input("Rock,paper or scissors?(r/p/s):").lower()
    if(user_choice not in choices):
        print("invalid input")
        continue
    computer_choice=random.choice(choices)
    print("your choice:",{emojis[user_choice]})
    print("computer's choice:",{emojis[computer_choice]})
    if(user_choice==computer_choice):
        print("tie")
    elif(
        (user_choice=="r" and computer_choice=="s")or
        (user_choice=="p" and computer_choice=="r")or
        (user_choice=="s" and computer_choice=="p")):
        print("you win ")
    else:
        print("you loose")
    again=input("continue?(y/n):").lower()
    if again=="n":
        print("Thanku for playing❤️")
        break
    elif(again!="y"):
        print("invalid")
    
    

