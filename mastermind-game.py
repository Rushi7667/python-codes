"""

"The Mastermind Game"

In This Game we used...
1.if-else statements
2.while loop
3.for loop

we used random function
to guess a number between 1000 to 10000
so system can guess 4 digit number.

->How It works?
When System guess any number it its memory
It will asks to enter a number.

If we entered the right number that system guess
It will show a massege shows our tries and wishings.

Otherwise It will askes next time untill right maches.
"We must enter right number to simmiler that number."

It will check Individually all the 4 integers.

And after the all right right choices It will greets us 
and shows the number of tries.

"""


# Code:


import random

num = random.randrange(1000,10000)

n = int(input("Enter the 4 digit number : " ))

if (n == num):
    print("Great! you guessed the number in just 1 try! You're Master Mind.")

else:

    notr = 0 # number of tries.

    while (n != num):
        notr += 1

        count = 0  # counts the integers.

        n = str(n)

        num = str(num)

        correct = ['X'] * 4  # Here X will save the correct value of integer.

        for i in range(0,4):# This loop will check the correct number till all the 4 digits will right. 
                                            
            if (n[i] == num[i]):            
                count += 1
                correct[i] = n[i]
                
            else:
                continue

        if (count < 4) and (count != 0):

            print("Not quite the number. But you did get" + " " + str(count) + " " + "digit(s) correct!.")
            print("Also these numbers in your input were correct.")

            for k in correct:       # This loop will add the integer into the right number if it will coreect.
                print(k, end=' ')
            print("\n")
            print("\n")

            n = int(input("Enter your next choice of numbers : "))

if n == num:
    print("You have become a Mastermind!")
    print("You took only" + " " + str(notr) + " " + "tries.")
