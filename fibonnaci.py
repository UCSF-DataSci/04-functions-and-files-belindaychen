#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse

#function to generate fib numbers les than a given limit
def generate_fibonacci(limit):
    fibonacci_list = []
    a, b = 0, 1 
    while a < limit: 
        fibonacci_list.append(a)
        a, b = b, a + b
    
    return fibonacci_list

#write the fibonacci_list to a file 
def write_to_file(fibonacci_list, file):
    try:
        with open(file, 'w') as f: 
            for number in fibonacci_list: 
                f.write(f"{number}\n")
        print(f"Fibonacci sequence successfully written to file.")
    except IOError as e: 
        print(f"Error writing to file")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers less than a limit and write to a file")
    parser.add_argument("limit", type=int, help="Upper limit for Fibonacci numbers.")
    parser.add_argument("output_file", type=str, help="Output file name.")

args = parser.parse_args()
    
fibonacci_sequence = generate_fibonacci(args.limit)
write_to_file(fibonacci_sequence, args.output_file)