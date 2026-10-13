# Task 13: Prime Number Analyzer

def is_prime(n):
    # 0, 1, and negative numbers are not prime
    if n <= 1:
        return False
    if n == 2:
        return True
    # even numbers greater than 2 cannot be prime
    if n % 2 == 0:
        return False

    # check odd divisors from 3 up to the square root of n
    limit = int(n ** 0.5)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False

    return True


def get_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def main():
    print("Welcome to the Prime Number Analyzer!")

    while True:
        print("\n--- Prime Number Analyzer Menu ---")
        print("1. Check if a number is prime")
        print("2. Generate primes in a range")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            try:
                user_input = input("Enter a number to check: ").strip()
                if user_input == "":
                    print("Input cannot be empty. Please type a whole number.")
                    continue

                num = int(user_input)
                result = is_prime(num)
                if result:
                    print(f"{num} is a prime number.")
                else:
                    print(f"{num} is not a prime number.")
            except ValueError:
                print("Invalid input! Please enter a whole number without letters or symbols.")

        elif choice == "2":
            try:
                start_input = input("Enter start of range: ").strip()
                end_input = input("Enter end of range: ").strip()

                if start_input == "" or end_input == "":
                    print("Input cannot be empty. Please enter both start and end numbers.")
                    continue

                start = int(start_input)
                end = int(end_input)

                if start > end:
                    print(f"Invalid range! Start number ({start}) cannot be greater than end number ({end}).")
                    continue

                result = get_primes_in_range(start, end)
                if len(result) > 0:
                    print(f"Prime numbers from {start} to {end}: {result}")
                    print(f"Total primes found: {len(result)}")
                else:
                    print(f"No prime numbers found between {start} and {end}.")
            except ValueError:
                print("Invalid input! Both start and end must be valid whole numbers.")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
