import random
min = 1
max = 100
number = random.randint(min,max)
print(f"Welcome player, today you will try your best to guess a number chosen by the computer, between {min} and {max} for now, by entering a number when asked to and trying to make more guesses based on the clues I give you.")

while True:
    range = input("Would you like to change the range of number the computer chooses from?: (Yes/No)\n").upper()
    number = random.randint(min,max)
    if range == "YES":
        min = int(input("Enter a minimum number the computer should pick from.\n"))
        max = int(input("Enter a maximum number the computer should pick from.\n"))
        number = random.randint(min,max)
    guess = input(f"Make you first guess, remember it is a number between {min} and {max}.\n")
    if guess.isdigit() == False:
       print("Trying to be sneaky? Please actually enter a number this time.") 
       guess = input(f"Enter a number, a number please, between {min} and {max}.\n")
    guess = int(guess)
    if guess < min or guess > max:
        print("This number is not within the range, try again. This attempt doesn't count.")
        guess = int(input(f"Enter a number between {min} and {max} this time.\n"))
    attempts = 1
    while guess != number:
        if guess > number:
            guess = int(input("Too high! Try again, enter another number.\n"))
            attempts += 1
        elif guess < number:
            guess = int(input("Too low! Try again, enter another number.\n"))
            attempts += 1
    print(f"Congratulations! You guessed the right number {number} in {attempts} tries.")
    print("Thank you for playing!!")
    again = input("Would you like to play again? (Yes/No)\n").upper()
    if again == "YES":
        continue
    else:
        break
print("Thank you for playing!")



