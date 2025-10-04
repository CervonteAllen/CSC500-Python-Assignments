# Week 1 - Part 2: Multiplication and Division
def main():
    print("Multiplication and Division")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    product = num1 * num2
    print(f"Product: {product}")
    if num2 == 0:
        print("Quotient: undefined (division by zero)")
    else:
        quotient = num1 / num2
        print(f"Quotient: {quotient}")

if __name__ == "__main__":
    main()
