import math
import random

lower = int(input("Enter the low number : ")) # user input lower number.

upper = int(input("Enter the upper number : ")) # user input upper number.

x = random.randint(lower , upper)

print("\n\tYou've only",round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n") # calculating the number of chances.

count = 0   #initially we take count 0

while count < math.log(upper - lower + 1,2):
    count += 1

    guess = int(input("guess the number : "))

    if x == guess:
        print("congratulations! You guessed right!")
        break

    elif x < guess:
        print("You guessed too high.")
    elif x > guess:
        print("You guessed too small.")
    
    if count > math.log(upper - lower + 1, 2):

        print("\nThe number is %d" % x)

        print("\tBetter Luck Next time!")