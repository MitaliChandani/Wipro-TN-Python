'''
1. Write a program to accept two numbers as command line argument and display their numbers.
'''
import sys

def display_numbers():
    if len(sys.argv) != 3:
        print("Provide two numbers")
        return
    num1 = sys.argv[1]
    num2 = sys.argv[2]

    print("First number:", num1)
    print("Second number:", num2)
display_numbers()

'''
2. Write a program to accept a welcome message to command-line argument and display the file name along with the welcome message.
'''
import sys

def show_welcome_message():
    if len(sys.argv) < 2:
        print("Welcome.")
        return
    
    file_name = sys.argv[0]
    welcome_message = ' '.join(sys.argv[1:])

    print("File name:", file_name)
    print("Welcome message:", welcome_message)
show_welcome_message()














