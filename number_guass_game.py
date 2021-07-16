"""In number guessing game we used if else statements and while loop.

we used random function for system so it can take any random integer.

we take math function for calculate the log.

also we have takken log base 2 for enough chances for users.

->How it works?

When user give the lower and upper value to the system...

System takes random integers from given range and gives chance to the user according to the range.

now user enter the value between that range and system check that the given value maches or not. if it is higher or lower than system pradict then it will shows, And if user lose all chance to guess than system reveals the value.

"""


# Code:


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
