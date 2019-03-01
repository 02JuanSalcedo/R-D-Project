"""
Key
C = User Chosen Input Operation
x = Global variable, The first number the user would operate with
y = Global variable, The second number the user would operate with
z = Local variable, The resulting number of the chosen operation
"""

# Declaring the types of operates the user cold use
print("Select an operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")

# Making the code look neater
print("")

# Gathering information from the user to calculate equation
C = input("Enter an operation 1/2/3/4/5: ")
x = input("Enter your first number: ")
y = input("Enter your second number: ")

# Making the code look neater
print("")

# Calculating an equation with the operation "+"
if C == "1":
    z = float(x) + float(y)
    (x + " " + "+" + " " + y + " " + "=" + " " + str(z))

# Calculating an equation with the operation "-"
elif C == "2":
    z = float(x) - float(y)
    print(x + " " + "-" + " " + y + " " + "=" + " " + str(z))

# Calculating an equation with the operation "*"
elif C == "3":
    z = float(x) * float(y)
    print(x + " " + "*" + " " + y + " " + "=" + " " + str(z))

# Calculating an equation with the operation "/"
elif C == "4":
    z = float(x) / float(y)
    print(x + " " + "/" + " " + y + " " + "=" + " " + str(z))

# Calculating an equation with the operation "^"
elif C == "5":
    z = float(x) ** float(y)
    print(x + " " + "^" + " " + y + " " + "=" + " " + str(z))
