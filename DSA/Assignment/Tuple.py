# 1. Print 4th element from start and end in a tuple
t = (10, 20, 30, 40, 50, 60, 70)
print("4th element from start:", t[3])
print("4th element from end:", t[-4])

# 2. Check whether an element exists in a tuple
t = (1, 3, 5, 7, 9)
element = 5
if element in t:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

# 3. Convert a list into a tuple
lst = [1, 2, 3, 4]
t = tuple(lst)
print("Converted Tuple:", t)

# 4. Find the index of an item in a tuple
t = ('a', 'b', 'c', 'd')
item = 'c'
index = t.index(item)
print(f"Index of '{item}':", index)

# 5. Replace last value of each tuple in a list with 100
lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = [t[:-1] + (100,) for t in lst]
print("Updated list:", updated_list)

