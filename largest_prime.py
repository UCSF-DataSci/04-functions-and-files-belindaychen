#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""
import argparse

#fibonacci sequence from previous question 
def generate_fibonacci(limit):
    fibonacci_list = []
    a, b = 0, 1
    while a < limit: 
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):  # Only check odd divisors
        if n % i == 0:
            return False
    return True

#to find largest prime fib number 
def largest_prime_fibonacci(limit):
    fibonacci_list = generate_fibonacci(limit)
    prime_fibs = [num for num in fibonacci_list if is_prime(num)]
    return max(prime_fibs) if prime_fibs else None 

if __name__ == "__main__":
    # Argument parsing for limit
    parser = argparse.ArgumentParser(description="Find the largest prime Fibonacci number below a limit.")
    parser.add_argument("limit", type=int, help="Upper limit for Fibonacci numbers.")
    
    args = parser.parse_args()

    # Find and print the largest prime Fibonacci number
    largest_prime_fib = largest_prime_fibonacci(args.limit)
    
    if largest_prime_fib:
        print(f"The largest prime Fibonacci number below {args.limit} is {largest_prime_fib}.")
    else:
        print(f"No prime Fibonacci numbers found below {args.limit}.")