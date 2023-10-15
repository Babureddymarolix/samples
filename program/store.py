def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if user_input == "add":
            print("Result:", add(num1, num2))
        elif user_input == "subtract":
          print("Result:", subtract(num1, num2))
        elif user_input == "divide":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please try again.")






# Initialize your budget
budget = 100000

# Prices of the appliances
washing_machine_price = 30000
fridge_price = 40000
cooler_price = 20000

# Check if you can afford each appliance
if budget >= washing_machine_price:
    print("You can buy a washing machine.")
    budget -= washing_machine_price
else:
    print("You can't afford a washing machine.")

if budget >= fridge_price:
    print("You can buy a fridge.")
    budget -= fridge_price
else:
    print("You can't afford a fridge.")

if budget >= cooler_price:
  print("You can buy a cooler.")
  budget -= cooler_price
else:
    print("You can't afford a cooler.")


