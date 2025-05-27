#lets make a game where the computer generates a random number then have two players pick a number and whomever is closest to the generated number wins!
import random

#have computer generate a random number
computer_number = random.randint(1, 100)
print("The random number has been generated! May the odds be forever in your favor!")

#ask each user to input their number
player_one_guess = int(input("Player ONE please enter a number : "))
player_two_guess = int(input("Player TWO please enter a number : "))

#calculate the difference in players guess and the random generated number
player_one_difference = abs(computer_number - player_one_guess)
player_two_difference = abs(computer_number - player_two_guess)

#reveal the generated number
print(f"\n The random generated number is : {computer_number}")

#decide who won
if player_one_difference < player_two_difference:
    print("Player ONE is the WINNER!")
elif player_two_difference < player_one_difference:
    print("Player TWO is the WINNER!")
else:
    print("It's a tie! Please pick another number!")