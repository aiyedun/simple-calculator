def calculator ():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operato(+,-,/,*)")
    num2 = float(input("Enter second number: "))
    
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error: Division by zero")

calculator()