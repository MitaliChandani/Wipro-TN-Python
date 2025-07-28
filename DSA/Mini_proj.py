''' 
Dictionary:
1. Create a dictionary that contains a list of people and one interesting fact about each of them.
Display each person and his or her interesting fact to the screen.
Next, change a fact about one of the people.
Also add an additional person and corresponding fact.
Display the new list of people and facts.
Run the program multiple times and notice if the order changes.
'''
people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("Original Facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

person_to_update = input("\nEnter the name of the person you want to update the fact for: ")
if person_to_update in people_facts:
    new_fact = input(f"Enter the new fact about {person_to_update}: ")
    people_facts[person_to_update] = new_fact
else:
    print(f"{person_to_update} is not in the list.")

new_person = input("\nEnter the name of a new person to add: ")
new_fact = input(f"Enter an interesting fact about {new_person}: ")
people_facts[new_person] = new_fact

print("\nUpdated Facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")


'''
List:
2. Given the participants score sheet for your University Sports Day,
you are required to find the runner-up score.
'''

scores = list(map(int, input("Enter the scores separated by space: ").split()))
max_score = max(scores)
filtered_scores = [score for score in scores if score != max_score]

runner_up_score = max(filtered_scores)
print("Runner-up score:", runner_up_score)

'''
3. Dictionary and List:
You have a record of n students. Each record contains the student's name,
and their percent marks in Math, Physics and Chemistry. The marks can be floating values.
You are required to save the record in a dictionary data type.
Students name is the key. Marks stored in a list is the value.
The user enters a student's name. Output the average percentage marks obtained by that student.
Formula: (sum of marks) / (no of subjects)


'''

records = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}
name = input("Enter a name: ")
if name in records:
    marks = records[name]
    average = sum(marks) / len(marks)
    print(f"Average percentage mark: {average}")
else:
    print("Student not found.")


'''
4. String:
Given a string of n words, help Alex to find out how many times his name appears in the string.
Constraint: 1 <= n <= 200
Sample input: Hi Alex WelcomeAlex Bye Alex.
Sample output: 3
Explanation: Alex name appears 3 times in the string. Hi Alex WelcomeAlex Bye Alex.
'''

text = input("Enter the string: ")
count = text.count("Alex")
print(count)


