''' Get the positive integer input from user.
keep on asking until the user enters a positive number'''


# input is positive integer : n >= 0
# when n < 0 I have to ask again 

n = int(float(input("Enter a positive number: ")))

while n < 0:
    print(f"The value: {n} entered is not a positive int!")
    n = int(float(input("Enter a positive number: ")))

print(f"Thanks for entering a positive num: {n}")
    
