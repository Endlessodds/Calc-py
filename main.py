x = float(input("Enter Number 1: "))
y = float(input("Enter Number 2: "))
operator = input('Choose any of these operators: (+, -, *, /): ')

def add(x, y):
    val = x + y
    return val

def sub(x, y):
    val = x - y
    return val

def mult(x, y):
    val = x * y
    return val

def div(x, y):
    if y == 0:
        print("Error: Cannot divide by zero")
        return None
    else:
        val = x / y
        return val

# Check the operator and perform the corresponding operation
if operator == '+':
    operator_name = 'Addition'
    result = add(x, y)
elif operator == '-':
    operator_name = 'Subtraction'
    result = sub(x, y)
elif operator == '*':
    operator_name = 'Multiplication'
    result = mult(x, y)
elif operator == '/':
    operator_name = 'Division'
    result = div(x, y)
else:
    print("Invalid operator. Please choose from +, -, *, /")
    result = None

# Print the result
if result is not None:
    print(f"The {operator_name} of {x} and {y} is {result}")
