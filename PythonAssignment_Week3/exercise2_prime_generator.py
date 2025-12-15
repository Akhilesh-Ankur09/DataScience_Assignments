# -------------------------------------------------
# Exercise 2: Prime Number Generator
# -------------------------------------------------
# This program:
# 1. Takes two positive integers as input
# 2. Validates the input
# 3. Finds all prime numbers in the given range
# 4. Displays 10 prime numbers per line
# 5. Handles invalid inputs gracefully
# -------------------------------------------------

try:
    # Take range input from user
    a = int(input("Enter start of range (positive integer): "))
    b = int(input("Enter end of range (positive integer): "))

    # Validate input
    if a <= 0 or b <= 0:
        raise ValueError("Numbers must be positive.")

    if a > b:
        raise ValueError("Start of range must be less than or equal to end.")

    primes = []

    # Function to check prime number
    for num in range(a, b + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)

    # Display primes (10 per line)
    print("\nPrime Numbers:")
    for i in range(0, len(primes), 10):
        print(" ".join(str(p) for p in primes[i:i + 10]))

except ValueError as ve:
    print("Input Error:", ve)

except Exception as e:
    print("Unexpected Error:", e)
