# Task 13: Prime Number Analyzer

## About the Program
This is a command-line Python program built for **Task 13: Prime Number Analyzer**. It lets you check whether a single number is prime and also generates all the prime numbers inside a range that you choose.

Main features:
- **Single Number Check**: Uses a reusable `is_prime(n)` function to check if a number is prime or not.
- **Range Generator**: Uses `get_primes_in_range(start, end)` to find and count every prime number between two numbers.
- **Input Validation**: Uses `try/except` and simple checks to handle letters, empty inputs, and invalid ranges (like when the start number is bigger than the end number) without crashing.

## How to Run It
1. Make sure Python 3 is installed on your computer.
2. Open a terminal inside the project folder.
3. Run the script with:
   ```bash
   python prime_analyzer.py
   ```

## How the Algorithm Works
Instead of dividing `n` by every single number from `2` to `n - 1`, `is_prime(n)` uses a few simple shortcuts so it runs much faster:

1. **Handling numbers 1 and below**: Numbers like `0`, `1`, and negative numbers are not prime by definition, so the function returns `False` right away if `n <= 1`.
2. **Skipping even numbers**: `2` is the only even prime number. Every other even number (`4`, `6`, `8`, `100`, etc.) can be divided by `2`. Once we return `True` for `2` and `False` for `n % 2 == 0`, we only have to check odd numbers (`3, 5, 7, ...`) using a step size of `2`. This cuts the number of checks in half.
3. **Checking only up to the square root of `n`**: Factors always come in pairs. For example, for `36`, the factor pairs are `(2, 18)`, `(3, 12)`, `(4, 9)`, and `(6, 6)`. If a number has a factor larger than its square root, it must also have a matching partner smaller than its square root. So if we check up to `int(n ** 0.5)` and still haven't found any divisor, no larger divisor can exist either, and the number is definitely prime.

## Sample Output
Below is the actual terminal output from my test run covering edge cases (`0`, `1`, `2`, `-7`), prime and composite numbers (`97`, `100`, `7919`), invalid inputs (`abc`, empty input), a valid range (`10` to `50`), and an invalid range (`50` to `10`):

```text
Welcome to the Prime Number Analyzer!

--- Prime Number Analyzer Menu ---
1. Check if a number is prime
2. Generate primes in a range
3. Exit
Enter your choice (1-3): 1
Enter a number to check: 0
0 is not a prime number.

--- Prime Number Analyzer Menu ---
1. Check if a number is prime
2. Generate primes in a range
3. Exit
Enter your choice (1-3): 1
Enter a number to check: 1
1 is not a prime number.

--- Prime Number Analyzer Menu ---
1. Check if a number is prime
2. Generate primes in a range
3. Exit
Enter your choice (1-3): 1
Enter a number to check: 2
2 is a prime number.

--- Prime Number Analyzer Menu ---
1. Check if a number is prime
2. Generate primes in a range
3. Exit
Enter your choice (1-3): 1
Enter a number to check: -7
-7 is not a prime number.

--- Prime Number Analyzer Menu ---
1. Check if a number is prime
2. Generate primes in a range
3. Exit
Enter your choice (1-3): 1
Enter a number to check: 97
97 is a prime number.

--- Prime Number Analyzer Menu ---
1. Check if a number is prime
2. Generate primes in a range
3. Exit
Enter your choice (1-3): 1
Enter a number to check: 100
100 is not a prime number.

--- Prime Number Analyzer Menu ---
1. Check if a number is prime
2. Generate primes in a range
3. Exit
Enter your choice (1-3): 1
Enter a number to check: 7919
7919 is a prime number.

--- Prime Number Analyzer Menu ---
1. Check if a number is prime
2. Generate primes in a range
3. Exit
Enter your choice (1-3): 1
Enter a number to check: abc
Invalid input! Please enter a whole number without letters or symbols.

--- Prime Number Analyzer Menu ---
1. Check if a number is prime
2. Generate primes in a range
3. Exit
Enter your choice (1-3): 1
Enter a number to check: 
Input cannot be empty. Please type a whole number.

--- Prime Number Analyzer Menu ---
1. Check if a number is prime
2. Generate primes in a range
3. Exit
Enter your choice (1-3): 2
Enter start of range: 10
Enter end of range: 50
Prime numbers from 10 to 50: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
Total primes found: 11

--- Prime Number Analyzer Menu ---
1. Check if a number is prime
2. Generate primes in a range
3. Exit
Enter your choice (1-3): 2
Enter start of range: 50
Enter end of range: 10
Invalid range! Start number (50) cannot be greater than end number (10).

--- Prime Number Analyzer Menu ---
1. Check if a number is prime
2. Generate primes in a range
3. Exit
Enter your choice (1-3): 3
Exiting program. Goodbye!
```

## Questions & Answers

**1. What is a prime number?**  
A prime number is a whole number greater than `1` that has only two positive divisors: `1` and itself. For example, `2`, `3`, `5`, `7`, and `97` are prime numbers because no other whole numbers divide them evenly. Numbers like `0` and `1` are not prime, and numbers greater than `1` with more than two factors (like `4`, `9`, or `100`) are called composite numbers.

**2. How do you optimize prime checking?**  
You can optimize prime checking in several steps:
- Immediately rule out numbers less than or equal to `1`.
- Handle `2` as a special case (return `True`), and immediately rule out all other even numbers (`n % 2 == 0`).
- Only loop up to the square root of `n` (`int(n ** 0.5)`) instead of `n - 1`, because any larger factor would already have a smaller partner below the square root.
- Step through the loop by `2` (`range(3, limit + 1, 2)`) so you only test odd divisors.
