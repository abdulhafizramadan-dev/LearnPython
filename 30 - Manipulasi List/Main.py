"""
## List Manipulation
1. Get specific item
2. Add new item in specific index
3. Add new item in the last list
4. Combine two list
5. Remove list
6. Remove last item in the list
"""

print(f"""
{10*"="} LIST MANIPULATION {"="*10}
""")

#          0/-3,    1/-2,    2/-1
names = ["Abdul", "Hafiz", "Ramadan"]
print(f"List names = \n{names}")

# Get specific item

# Get first item
firstname = names[0]
print(f"First name = {firstname}")

# Get last item
# lastname = names[len(names)-1]
lastname = names[-1]
print(f"Last name = {lastname}")

# Add new item in specific index
names.insert(1, "Muslim")
print(f"List names = \n{names}")

# Add new item in the last of list
names.append("Ridho")
names.append("Elsa")
print(f"List names = \n{names}")

# Combine two list
names_of_sister_in_law = ["Ike", "Putri"]
names.extend(names_of_sister_in_law)
print(f"List names = \n{names}")

# Remove List
names.remove("Ramadan")
# names.remove("Dadang")  # Will throw an error = ValueError: list.remove(x): x not in list
print(f"List names = \n{names}")

# Remove last item in the list
popped_name = names.pop()
print(f"List names = \n{names}")

print(f"Popped name = {popped_name}")

