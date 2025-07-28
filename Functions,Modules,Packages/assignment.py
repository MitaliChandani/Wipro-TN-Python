#Functions:
'''
1. Write a function to return the sum of all numbers in a list
Sample list: (8,2,3,0,7)
Expected output: 20
'''
def sum_of_list():
    user_input = input("Enter no.: ")
    numbers = list(map(int, user_input.split()))
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum of list:", sum_of_list())

'''
2. Write a function to return the reverse of a string.
Sample string: "1234abcd"
Expected output: "dcba4321"
'''
def reverse_string_elements():
    user_input = input("Enter characters: ")
    elements = [item.strip() for item in user_input.split(',')]
    reversed_elements = elements[::-1]
    return ', '.join(reversed_elements)

print("Reversed string:", reverse_string_elements())

'''
3. Write the function to calculate and return the factorial of a number (a Non-negative integer)
'''
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input("Enter a non-negative integer: "))
print("Factorial:", factorial(num))

'''
4. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters in it.
'''
def count_letters():
    text = input("Enter a string: ")
    uppercase_count = 0
    lowercase_count = 0

    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    print("Uppercase letters:", uppercase_count)
    print("Lowercase letters:", lowercase_count)
count_letters()

'''
5. Write a function to print the even numbers from a given list. List is passed to the function as an argument.
Sample list is [1,2,3,4,5,6,7,8,9]
Expected result: [2,4,6,8]
'''
def print_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", ''.join(map(str, even_numbers)))

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even_numbers(sample_list)

'''
6. Write a function that takes a number as parameter and checks whether the number is prime or not.
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")



