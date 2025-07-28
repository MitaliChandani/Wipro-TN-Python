# 1. Write a program to count the number of upper and lower case letters in a string.
s = "HelloWorld"
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

# 2. Write a program that will check whether a given string is palindrome or not.
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# 3. Given a string, return a new string made of n copies of the first 2 chars of the original string
# where n is the length of the string. The string length will be >= 2.
# Example: If input is "Wipro" then output should be "WiWiWiWiWi".
s = "Wipro"
n = len(s)
new_str = s[:2] * n
print("Result:", new_str)


#4. Given a string, if the first or last character is 'x', return the string without those 'x' characters,
#else return the string unchanged. 
#Example: If the input is "xHix", then output is "Hi".

s = "xHix"
if s.startswith('x'):
    s = s[1:]
if s.endswith('x'):
    s = s[:-1]
print("Result:", s)

# 5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
# Example: If the inputs are “Wipro” and 3, then the output should be “propropro”.

s = "Wipro"
n = 3
last_n = s[-n:]
result = last_n * n
print("Result:", result)
