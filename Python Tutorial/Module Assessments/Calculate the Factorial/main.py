def main():

    num = int(input("Enter a number to calculate its factorial: "))

    # Check if the number is non-negative
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Initialize the factorial result
        factorial = 1

        # Calculate the factorial
        for i in range(1, num + 1):
            factorial *= i

        # Print the result
        print(f"The factorial of {num} is: {factorial}")

if __name__ == "__main__":
    main()
