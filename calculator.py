# addition
def add(a, b):
    return a + b

# subtraction
def subtract(a, b):
    return a - b

# multiplication
def multiply(a, b):
    return a * b

# division
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    else:
        return a / b

# given operators
def choose_operator():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    # if its true then choose operator
    while True:
        choice = input("Enter choice(1,2,3,4): ")
        # check if the input is valid choice
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("enter first number: "))
                num2 = float(input("enter second number: "))
            except ValueError:
                print("invalid input")
                continue
            if choice == "1":
                print(f"the result of {num1}+{num2} is: {add(num1, num2)}")
            elif choice == "2":
                print(f"the result of {num1}-{num2} is: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"the result of {num1}*{num2} is: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"the result of {num1}/{num2} is: {divide(num1, num2)}")
        else:
            print("invalid choice")
        next_calculator = input("do you want perform another calculator?(yes/no: )")
        if next_calculator.lower() != "yes":
            break

# Call the choose_operator function
choose_operator()