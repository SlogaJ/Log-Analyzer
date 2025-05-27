#Ask the first person to input their age, implement input validation.
try:
    my_age = int(input("Please enter your age: "))
    if my_age < 1 or my_age > 120:
        print ("Invalid input, please enter a number between 1 - 120")
    else:
        print (f"You are {my_age} years old!")
except ValueError:
    print("Invalid input, please enter a valid number!")

#Ask the second person to input their age, implement input validation.
try:
    your_age = int(input("Please enter the second persons age: "))
    if your_age < 1 or your_age > 120:
        print("Number is not in valid range, please enter again.")
    else:
        print(f"The second person is {your_age} years old!")
except ValueError:
    print("Invalid input, please enter a valid number!")

#Get the difference in age by years between the two
age_difference = abs(my_age - your_age)

print (f"The difference in age between the two is {age_difference} years!")

#Ask which month the first user was born in, implement input validation.
valid_months = [
    "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"
]
try:
    user_one_month = input("Please enter the month you were born: ").lower()
    if user_one_month not in valid_months:
        print ("Invalid input! Please enter one of the twelve months.")
    else:
        print (f"The month you were born in is: {user_one_month.capitalize()}!")
except ValueError:
    print("Invalid input! Please try again.")

#Ask the second user which month they were born in, implement input validation.
try:
    user_two_month = input("Please enter the month you were born: ").lower()
    if user_two_month not in valid_months:
        print ("Invalid input! Please enter one of the twelve months.")
    else:
        print(f"The month you were born in is: {user_two_month.capitalize()}!")
except ValueError:
    print("Invalid Input! Please try again.")


