''' 
1. Write a Python function that accepts a hyphen-separated sequence of colors
as input and returns the colors in a hyphen-separated sequence after sorting
them alphabetically.
Constraint: All the colors will be completely in either lower case or upper case.
Sample input 1: green-red-yellow-black-white
Sample output 1: black-green-red-white-yellow

Sample input 2: PINK-BLUE-TAN-PURPLE
Sample output 2: BLUE-PINK-PURPLE-TAN
'''
def sort_colors(color_sequence):
    colors = color_sequence.split('-')
    colors.sort()
    return '-'.join(colors)
print(sort_colors("green-red-yellow-black-white"))
print(sort_colors("PINK-BLUE-TAN-PURPLE"))

'''
2.
ispalindrome(name)
Given the user name as input, this function should tell us whether the name is a palindrome or not.
count_the_vowels(name)
Given the user name as input, this function should tell us how many vowels are present in it.
frequency_of_letters(name)
Given the user name as input, this function should tell us how many times each letter appears in the name.
Note:
The input name will be completely in either lowercase or uppercase.
Import this module in another Python script and test the functions by passing appropriate inputs.

Sample input 1: bob
Sample output 1:
Yes it is a palindrome.
No of vowels: 1
Frequency of letters: b-2, o-1

Sample input 2: marcel bentok tanaka
Sample output 2:
No it is not a palindrome.
No of vowels: 7
Frequency of letters: m-1, a-4, r-1, c-1, e-2, l-1, b-1, n-2, t-2, o-1, k-2
'''
def ispalindrome(name):
    return name == name[::-1]

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    return sum(1 for char in name if char in vowels)

def frequency_of_letters(name):
    freq = {}
    for char in name.replace(" ", ""):
        freq[char] = freq.get(char, 0) + 1
    return freq

