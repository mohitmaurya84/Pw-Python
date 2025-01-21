# 1. Sum of all even numbers in a list
def sum_of_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

# Example
nums = [1, 2, 3, 4, 5, 6]
print(sum_of_even_numbers(nums))

# 2. Reverse a string
def reverse_string(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

# Example
text = "Mohit"
print(reverse_string(text))

#3. Squares of each number in a list
def square_numbers(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num ** 2)
    return squared_list

# Example
nums = [1, 2, 3, 4]
print(square_numbers(nums))

#4. Check if a number is prime (1 to 200)
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example
primes = [n for n in range(1, 201) if is_prime(n)]
print(primes)

#5. Iterator class for Fibonacci sequence
class FibonacciIterator:
    def __init__(self, terms):
        self.terms = terms
        self.current, self.next = 0, 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.terms:
            raise StopIteration
        value = self.current
        self.current, self.next = self.next, self.current + self.next
        self.index += 1
        return value

# Example
fib = FibonacciIterator(10)
for num in fib:
    print(num, end=" ")

#6. Generator for powers of 2
def powers_of_two(max_exponent):
    for exponent in range(max_exponent + 1):
        yield 2 ** exponent

# Example
for power in powers_of_two(5):
    print(power, end=" ")

#7. File reader generator
def file_line_reader(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print("File not found!")

#8. Sort a list of tuples by the second element
tuples_list = [(1, 3), (4, 1), (2, 5)]
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(sorted_list)

#9. Convert Celsius to Fahrenheit using map()
def celsius_to_fahrenheit(celsius_list):
    return list(map(lambda c: (c * 9/5) + 32, celsius_list))

# Example
celsius = [0, 20, 30]
print(celsius_to_fahrenheit(celsius))

#10. Remove vowels using filter()
def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join(filter(lambda char: char not in vowels, string))

# Example
text = "Mohit loves Python"
print(remove_vowels(text))

