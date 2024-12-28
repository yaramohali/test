def main():
    count = int(input("Enter the number of Fibonacci numbers to display: "))

    # Check if the count is valid
    if count <= 0:
        print("Please enter a positive integer.")
    else:
        # Initialize the first two Fibonacci numbers
        fib_sequence = [0, 1]

        # Generate the Fibonacci sequence up to the specified count
        while len(fib_sequence) < count:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

        # Print the sequence up to the count
        print(f"Fibonacci sequence (first {count} numbers):", fib_sequence[:count])

if __name__ == "__main__":
    main()
