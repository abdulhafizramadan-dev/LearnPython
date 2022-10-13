from copy import deepcopy

# Copy
print(f"""
{10*"="} COPY {"="*10}
""")

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

nested_numbers = [numbers1, numbers2]
nested_numbers_copy = nested_numbers.copy()

print(f"Number =\n{nested_numbers}")
print(f"Number Copy =\n{nested_numbers_copy}")

print()

print(f"Number memory address \t\t= {hex(id(nested_numbers))}")
print(f"Number copy memory address \t= {hex(id(nested_numbers_copy))}")

print()

print(f"Number index 0 memory address = {hex(id(nested_numbers[0]))}")
print(f"Number copy index 0 memory address = {hex(id(nested_numbers_copy[0]))}")

numbers1[1] = 200
print()

print(f"Number =\n{nested_numbers}")
print(f"Number Copy =\n{nested_numbers_copy}")


# Using Deep Copy
print(f"""
{10*"="} DEEP COPY {"="*10}
""")

nested_numbers_deepcopy = deepcopy(nested_numbers)

print(f"Number memory address \t\t\t= {hex(id(nested_numbers))}")
print(f"Number copy memory address \t\t= {hex(id(nested_numbers_copy))}")
print(f"Number deepcopy memory address \t= {hex(id(nested_numbers_deepcopy))}")

print()

print(f"Number index 0 memory address = {hex(id(nested_numbers[0]))}")
print(f"Number copy index 0 memory address = {hex(id(nested_numbers_copy[0]))}")
print(f"Number deepcopy index 0 memory address = {hex(id(nested_numbers_deepcopy[0]))}")

numbers1[1] = 2
print()


print(f"Number =\n{nested_numbers}")
print(f"Number Copy =\n{nested_numbers_copy}")
print(f"Number DeepCopy =\n{nested_numbers_deepcopy}")
