while True:
    value1 = int(input("Enter your 1st value: "))
    sign = input("Enter operator (+, -, *, /) or 'q' to quit: ")
    
    if sign.lower() == 'q':
        print("Calculations Terminated by you")
        break
        
    value2 = int(input("Enter your 2nd value: "))
    if sign == "+":
        print("Sum: ", value1 + value2)
    elif sign == "-":
        print("Difference: ", value1 - value2)
    elif sign == "*":
        print("Product: ", value1 * value2)
    elif sign == "/":
        if value2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Division:", value1 / value2)
    else:
        print("Invalid operator! Please use +, -, *, or /")
