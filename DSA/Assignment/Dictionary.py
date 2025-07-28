# 1. Add a key and value to a dictionary
d = {0: 10, 1: 20}
d[2] = 30
print("Updated Dictionary:", d)

# 2. Concatenate multiple dictionaries into one
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {}

for d in (dic1, dic2, dic3):
    result.update(d)
print("Concatenated Dictionary:", result)

# 3. Check if a given key exists in a dictionary
d = {1: 100, 2: 200, 3: 300}
key = 2
if key in d:
    print(f"Key {key} exists in the dictionary.")
else:
    print(f"Key {key} does not exist.")

# 4. Iterate over a dictionary and print keys, values, and both
d = {'a': 1, 'b': 2, 'c': 3}
print("Keys:")
for key in d:
    print(key)

print("Values:")
for value in d.values():
    print(value)
print("Keys and Values:")
for key, value in d.items():
    print(f"{key}: {value}")

# 5. Create a dictionary with keys from 1 to 15 and values as their squares
squares = {x: x**2 for x in range(1, 16)}
print("Squares Dictionary:", squares)

# 6. Sum all the values in a dictionary
d = {'a': 10, 'b': 20, 'c': 30}
total = sum(d.values())
print("Sum of all values:", total)
