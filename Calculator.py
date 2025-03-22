print("Hello World")
# loop it forever
while True:
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    operation = input("Enter the operation you want to perform (+, -, *, /): ")
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        result = "Cannot divide by zero" if b == 0 else a / b
    else:
        result = "Invalid operation"

    print(f"Result: {result}")
    if input("Exit? ").lower() == 'yes':
        break
