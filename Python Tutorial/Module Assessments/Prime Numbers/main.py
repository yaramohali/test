def main():
    N = int(input("Enter a number to find all prime numbers up to: "))
    # Check if N is greater than or equal to 2
    if N < 2:
        print("No prime numbers exist less than 2.")
    else:
        print(f"Prime numbers between 2 and {N} are:")
        # Loop through all numbers from 2 to N
        for num in range(2, N + 1):
            # Assume num is prime until proven otherwise
            is_prime = True
            # Check divisors from 2 to the square root of num
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:  # If divisible, num is not prime
                    is_prime = False
                    break
            if is_prime:
                print(num, end=" ")

if __name__ == "__main__":
    main()
