#ASSIGNMENT:
# Q1. Program to check if a number is Positive, Negative or Zero
num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

# Q2. Program to check if a number is Odd or Even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# Q3. Program to check if two non-negative numbers have the same last digit
num1 = int(input("Enter first no.: "))
num2 = int(input("Enter second no.: "))

if num1 % 10 == num2 % 10:
    print("Same last digit.")
else:
    print("Different last digits.")

# Q4. Program to print numbers from 1 to 10 in a single row with tab space
for i in range(1, 11):
    print(i, end="\t")

# Q5. Program to print even numbers between 23 and 57
for a in range(23, 58):
    if a % 2 == 0:
        print(a)

# Q6. Write a program to check if a given number is prime or not.
n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, int(n / 2) + 1):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")

# Q7. Program to print all prime numbers between 10 and 99
for n in range(10, 100):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                break
        else:
            print(n)

# Q8. Write a program to print the sum of all the digits of a given number.
num = input("Enter a number: ")
sum_of_digits = 0

for digit in num:
    sum_of_digits += int(digit)
print("Sum of digits:", sum_of_digits)

# Q9. Write a program to reverse a given number and print.
num = input("Enter a number: ")
reverse = num[::-1]
print("Reversed number:", reverse)

# Q10. Write a program to find if the given number is palindrom or not.
num = input("Enter a number: ")
if num == num[::-1]:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")
