a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

z = input("Enter the opration : ")

if z=='+':
    x = int(a) + int(b)
    print("sum of {} and {} is : {}".format(a,b,x))
elif z=='-':
    x = int(a) - int(b)
    print("subtraction of {} and {} is : {}".format(a,b,x))
elif z=='*':
    x = int(a) * int(b)
    print("multiplication of {} and {} is : {}".format(a,b,x))
elif z=='/':
    x = int(a) / int(b)
    print("division of {} and {} is : {}".format(a,b,x))
