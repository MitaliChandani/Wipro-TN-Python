# 1. Program to read the entire content from a text file and display it to the user

file_name = input("Enter name of the text file: ")
file = open(file_name, 'r')
content = file.read()
print("\n--- File Content ---\n")
print(content)

file.close()

# 2. Write a program to read first n lines from a txt file, Get n as user input

file_name = input("Enter name of the text file: ")
n = int(input("Enter the number of lines to read: "))

file = open(file_name, 'r')

print(f"\n First {n} line(s) of the file\n")
for i in range(n):
    line = file.readline()
    if not line:
        break
    print(line.strip())

file.close()

# 3. Program to accept input from the user and append it to a text file

file_name = input("Enter the name of the text file: ")
user_text = input("Enter the text you want to append: ")

file = open(file_name, 'a')
file.write(user_text + '\n')
file.close()

print("Text appended")

# 4. Program to find the longest word from each line of a text file and store them in a list

file_name = input("Enter the text file name: ")
file = open(file_name, 'r')

longest_words = []

for line in file:
    words = line.strip().split()
    if words:
        longest_word = max(words, key=len)
        longest_words.append(longest_word)
file.close()
print("\nLongest word from each line:")
print(longest_words)

# 5. Program to find the longest word from the contents of a text file

file_name = input("Enter the text file name: ")
file = open(file_name, 'r')

content = file.read()
words = content.split()
longest_word = max(words, key=len)

file.close()
print("The longest word in the file is:", longest_word)

# 6. Program to count the frequency of a user-entered word in a text file

file_name = input("Enter the text file name: ")
search_word = input("Enter the word to count: ")

file = open(file_name, 'r')
content = file.read()
words = content.split()
count = words.count(search_word)
file.close()
print(f"The word '{search_word}' appears {count} time(s) in the file.")
