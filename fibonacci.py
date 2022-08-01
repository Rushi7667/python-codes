x = int(input("Enter the steps of fibonacci series : "))
n1=0
print("0")
n2=1
print("1")
n3=n1+n2
for i in range(x):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)