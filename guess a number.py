
import random
number = random.randint(1,100)

#let the user see their shits
while True:
    guess = int(input("guess a number: "))
    if guess < number:
        print("too low")
        continue
    elif guess > number:
        print("too high")
        continue
    elif guess == number:
        print("correct")
        break