'''
Write a Python program to decode a secret message from a text file.
The file contains multiple lines of text. Determine the meeting time based on the number of lines in the file:
If lines > 12, subtract 12 to get PM time.
Otherwise, it’s AM time.
Also, find the most frequently occurring word in the file (ignoring case and punctuation).
Capitalize it and display it as the meeting place followed by 'Street'.
'''
file_name = input("Enter the file name (with .txt extension): ")
file = open(file_name, 'r')
lines = file.readlines()
file.close()

line_count = len(lines)
if line_count > 12:
    meeting_hour = line_count - 12
    meridian = "PM"
else:
    meeting_hour = line_count
    meridian = "AM"

word_freq = {}
for line in lines:
    words = line.strip().split()
    for word in words:
        clean_word = word.strip(".,!?;:\"").capitalize()
        if clean_word:
            word_freq[clean_word] = word_freq.get(clean_word, 0) + 1

max_word = max(word_freq, key=word_freq.get)
print(f"\nMeeting time: {meeting_hour} {meridian}")
print(f"Meeting place: {max_word} Street")
