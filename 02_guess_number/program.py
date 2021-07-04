import random

print('------------------------------')
print('     GUESS THAT NUMBER GAME   ')
print('------------------------------')
print()

the_number = random.randint(0,100)
guess = -1

name = input("What is your name?")

# print("The secret number is: ", the_number)
# print("Your guess was: ", guess)

while guess != the_number:
    guess_text = input("Guess a # between 0 and 100:  ")
    guess = int(guess_text)
    if guess < the_number:
        print("Sorry {}, your guess of {} was too low".format(name,guess))
    elif guess > the_number:
        print("Sorry {}, your guess of {} was too high".format(name,guess))
    else:
        print("Great work, {}, you win! It was {}.".format(name,the_number))

print('Game over.')