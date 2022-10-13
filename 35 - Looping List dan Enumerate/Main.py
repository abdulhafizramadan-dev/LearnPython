"""
## List Looping
1. For Loop
2. For Loop and Range
3. While
4. List Comprehension
5. Enumerate
"""

names = ["Abdul", "Hafiz", "Ramadan"]

# For Loop
print(f"""
{10*"="} LOOPING LIST USING FOR LOOP {"="*10}
""")

for name in names:
    print(f"Name -> {name}")


# For Loop and Range
print(f"""
{10*"="} LOOPING LIST USING FOR LOOP AND RANGE {"="*10}
""")

for index in range(len(names)):
    print(f"Index - {index} | {names[index]}")


# While Loop
print(f"""
{10*"="} LOOPING LIST USING WHILE LOOP {"="*10}
""")

index = 0
while index < len(names):
    print(f"Index - {index} | {names[index]}")
    index += 1


# List Comprehension
print(f"""
{10*"="} LOOPING LIST USING LIST COMPREHENSION {"10"*10}
""")

[print(f"Name -> {name}") for name in names]


# Enumerate
print(f"""
{10*"="} LOOPING LIST USING ENUMERATE {"="*10}
""")

for index, name in enumerate(names):
    print(f"Index - {index} | {name}")
