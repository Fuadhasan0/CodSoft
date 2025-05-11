def get_number(prompt: str) -> float:
    """Get valid numerical input from user with retry logic"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation() -> str:
    """Get valid arithmetic operation from user"""
    valid_ops = {'+', '-', '*', '/'}
    while True:
        op = input("Choose operation (+, -, *, /): ").strip()
        if op in valid_ops:
            return op
        print("Invalid operation. Please choose from +, -, *, /")

def calculate(num1: float, num2: float, op: str) -> float:
    """Perform calculation based on operator with error handling"""
    try:
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError
            return num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed!"

def main():
    print("\n" + "="*30)
    print("PYTHON CALCULATOR")
    print("="*30)
    
    while True:
        # Get user inputs
        num1 = get_number("\nEnter first number: ")
        num2 = get_number("Enter second number: ")
        op = get_operation()

        # Perform calculation
        result = calculate(num1, num2, op)
        
        # Display result
        print(f"\nResult: {num1} {op} {num2} = {result}")

        # Continue prompt
        continue_calc = input("\nAnother calculation? (y/n): ").lower()
        if continue_calc != 'y':
            print("\nThank you for using the calculator!")
            break

if __name__ == "__main__":
    main()