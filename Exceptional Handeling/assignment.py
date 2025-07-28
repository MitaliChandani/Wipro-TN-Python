# 1. Write a Python program to accept two numbers from the user and perform division. If any exception occurs, print an error message. Otherwise, print the result.
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
except Exception as e:
    print("An error occurred:", e)
else:
    print("Result of division:", result)

# 2. Write a program to accept a number from the user and check whether it's prime or not. If the user enters anything other than a number, handle the exception and print an error message.

try:
    num = int(input("Enter a number: "))
    if num <= 1:
        print("Not a prime number.")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("Not a prime number.")
                break
        else:
            print("Prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


# 3. Write a program to accept the file name to be opened from the user. If the file exists, print the content of the file in title case. Otherwise, handle the exception and print an error message.
try:
    file_name = input("Enter the file name: ")
    file = open(file_name, 'r')
    content = file.read()
    print("\nFile Content in Title Case\n")
    print(content.title())
    file.close()
except FileNotFoundError:
    print("Error: The file does not exist.")

'''
4. Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number.
If any invalid index is entered, handle the exception and print an error message. Declare a list with 10 integers
'''
numbers = [5, -3, 12, -7, 9, 0, -1, 4, -6, 8]

try:
    index = int(input("Enter an index (0 to 9): "))
    value = numbers[index]
    
    if value > 0:
        print(f"The number at index {index} is positive.")
    elif value < 0:
        print(f"The number at index {index} is negative.")
    else:
        print(f"The number at index {index} is zero.")

except IndexError:
    print("Error: Invalid index! Please enter a number between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer.")
