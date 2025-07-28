# 1. Write a program to check if a string has only octal digits. Given string ['789','123','004']
import re
strings = ['789','123','004']
for s in strings:
    if re.fullmatch(r'[0-7]+', s):
        print(f"{s} -> Octal")
    else:
        print(f"{s} -> Not Octal")


# 2. Extract the user id, domain name and suffix from the following email addresses.
import re
emails = ["zuck@facebook.com", "sunder33@google.com", "jeff42@amazon.com"]
for email in emails:
    match = re.match(r'(\w+)@(\w+)\.(\w+)', email)
    if match:
        print(f"User: {match.group(1)}, Domain: {match.group(2)}, Suffix: {match.group(3)}")

# 3. Split the following irregular sentence into proper words
import re
sentence = "A, very; very: irregular_sentence"
words = re.split(r'[;,_:\s]+', sentence)
print(" ".join(words))

#6. Find words that start and end with same letter
import re
words = ['civic','trust','widows','maximum','museums','aa','as']
for word in words:
    if re.match(r'^(.).*\1$', word):
        print(word)
