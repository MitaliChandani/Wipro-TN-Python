# 1. Create a list of 5 integers and display list items using index
nums = [10, 20, 30, 40, 50]
for i in range(len(nums)):
    print(f"Element at index {i} is {nums[i]}")

# 2. Append a new item to the end of the list
nums = [10, 20, 30]
nums.append(40)
print("Updated list:", nums)

# 3. Reverse the order of the items in the list
nums = [1, 2, 3, 4, 5]
nums.reverse()
print("Reversed list:", nums)

# 4. Print the number of occurrences of a specified element in a list
nums = [1, 2, 3, 2, 4, 2]
element = 2
print(f"{element} occurs {nums.count(element)} times")

# 5. Append the items of list1 to list2 at the front
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print("Combined list:", result)

# 6. Insert a new item before the second element in an existing list
nums = [10, 20, 30, 40]
nums.insert(1, 15)
print("Updated list:", nums)

# 7. Remove the item from a specified index in a list
nums = [100, 200, 300, 400]
index = 2
nums.pop(index)
print("List after removing index 2:", nums)

# 8. Remove the first occurrence of a specified element from a list
nums = [5, 3, 7, 3, 9]
element = 3
nums.remove(element)
print("List after removing first occurrence of 3:", nums)
