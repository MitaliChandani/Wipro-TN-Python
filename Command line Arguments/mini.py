'''
Program Description:
Through command-line arguments, three strings separated by space are given to you.
Each string is a series of numbers separated by hyphen (-).
You like all the numbers in string 1 and dislike all the numbers in string 2.
The third string contains the numbers given to you.
 
Rules:
Your initial happiness is 0.
For each number in the third string:
If it's in string 1 → +1 happiness.
If it's in string 2 → -1 happiness.
Otherwise → no change. 
Output the final happiness score at the end.

Sample input:
python happiness_score.py 3-1 5-7 1-5-3-8
Sample output:
1
'''
import sys

like_str = sys.argv[1]
dislike_str = sys.argv[2]
given_str = sys.argv[3]

likes = list(map(int, like_str.split('-')))
dislikes = list(map(int, dislike_str.split('-')))
given = list(map(int, given_str.split('-')))

happiness = 0

for num in given:
    if num in likes:
        happiness += 1
    elif num in dislikes:
        happiness -= 1
print(happiness)
