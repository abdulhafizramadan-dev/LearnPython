"""
## List Operation
1. Count -> how many data in the list
2. Sort -> sort the entire list in ascending format
3. Reverse -> reversed the entire list
"""

numbers = [2, 2, 4, 2, 5, 1, 6, 6, 2, 6, 7, 10, 19]
names = ["Abdul", "Hafiz", "Ramadan"]

print(f"Data numbers = \n{numbers}")
print(f"Data names = \n{names}")

# Count
data_count_2 = numbers.count(2)
data_count_6 = numbers.count(6)

print(f"Many number 2 in numbers = {data_count_2}")
print(f"Many number 6 in number = {data_count_6}")

# Sort
print(f"Data numbers before sort =\n{numbers}")
numbers.sort()  # Sort the list Ascending
# numbers.sort(reverse=True)  # Sort the list Descending
print(f"Data numbers after sort = \n{numbers}")

# Reverse
print(f"Data names before reverse = \n{names}")
names.reverse()
print(f"Data names after reverse = \n{names}")

