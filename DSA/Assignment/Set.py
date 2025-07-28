# 1. Remove a given item from the set
s = {1, 2, 3, 4, 5}
s.discard(3)
print("Updated set:", s)

# 2. Create an intersection of sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1 & set2
print("Intersection:", intersection)

# 3. Create a union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2
print("Union:", union)

# 4. Find the maximum and minimum value in a set
s = {10, 25, 5, 40, 15}
print("Maximum value:", max(s))
print("Minimum value:", min(s))
