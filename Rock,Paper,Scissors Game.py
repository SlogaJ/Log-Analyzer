#Let's Play some Rock, Papper, Scissors!
import random

#showcase the three options
options = ["rock", "paper", "scissors"]
print("Players! the options we have today are Rock, Paper, or Scissors!")

#player one makes their choice
print("Player ONE make your choice!")
player_ones_choice = input("").lower()

computers_choice = random.choice(options)

#reveal what was chosen
print(f"\nYou chose {player_ones_choice}")
print(f"The computer chose {computers_choice}\n")

#decide who won
if player_ones_choice == computers_choice:
    print("Draw!")
elif player_ones_choice == "rock":
    if computers_choice == "scissors":
        print("Winner! You're really good at this!")
    else:
        print("Womp Womp, better luck next time!")

elif player_ones_choice == "paper":
    if computers_choice == "rock":
        print("You're a winner winner chicken dinner!")
    else:
        print("Dang maybe choose a better option!")
else:
    print("Hey! Thats not one of the provided options! Try again!")






#player two makes their choice
#print("Player TWO make your choice!")
#player_twos_choice = input("")



