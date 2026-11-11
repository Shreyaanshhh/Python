
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

# 1. append() - Adds an element at the end
friends.append("Shreyanshh")
print("Append:", friends)

# 2. sort() - Sorts the list (ascending order)
l1 = [1, 34, 62, 2, 6, 11]
l1.sort()
print("Sort:", l1)

# 3. reverse() - Reverses the list
l1.reverse()
print("Reverse:", l1)

# 4. insert() - Inserts an element at a specific index
l1.insert(2, 333333)
print("Insert:", l1)

# 5. pop() - Removes and returns an element at a given index
value = l1.pop(3)
print("Pop Value:", value)
print("After Pop:", l1)

# 6. remove() - Removes a specific element
l1.remove(34)
print("Remove:", l1)

# 7. copy() - Creates a copy of the list
new_list = l1.copy()
print("Copy:", new_list)

# 8. count() - Counts occurrences of an element
numbers = [1, 2, 3, 1, 1, 4]
print("Count:", numbers.count(1))

# 9. index() - Returns the index of an element
print("Index:", numbers.index(3))

# 10. extend() - Adds multiple elements to a list
l1.extend([100, 200, 300])
print("Extend:", l1)

# 11. clear() - Removes all elements
new_list.clear()
print("Clear:", new_list)
