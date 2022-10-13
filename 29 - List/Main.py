# Int List
numbers = [1, 2, 3, 4, 5]
print(f"Numbers -> {numbers}")

# String List
names = ["Abdul", "Hafiz", "Ramadan"]
print(f"Names -> {names}")

# Alternative Making List

# Using Range
range_list = list(range(2, 11, 2))  # range(start, stop, step)
print(f"Range List -> {range_list}")

# Using For Loop
for_list = [i for i in range(10)]
print(f"For List -> {for_list}")

# Custom For item
for_list = [i*2 for i in range(10)]
print(f"For List -> {for_list}")

# Condition For item
for_list = [i for i in range(10) if i % 2]
print(f"For List -> {for_list}")
