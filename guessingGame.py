import random

print('Number Guessing Game')

number = random.randint(1,9)

chances = 0

print('guess a number between 1 - 9')

while chances < 5:
    guess = int(input('enter your guess: '))

    if guess == number:  
        print('Congrats! you won')
        break
    elif guess < number:
        print('Your guess is too low. Guess a number higher than ', guess)
    else:
        print('Your guess was too high. Guess a number higher than ', guess)
    
    chances = chances + 1

if not chances < 5:
    print('You lose and the number is ', number)