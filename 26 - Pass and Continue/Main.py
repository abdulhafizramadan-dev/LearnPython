# Pass -> Dummy implementation like TODO
header = f"""
{10*"="} PASS {"="*10}
"""
print(header)

number = 0
while number < 5:
    number += 1
    if number % 2 == 0:
        pass  # Nothing do anything, but if you remove this. will should make the implementation of it
    print(f"Number -> {number}")

# Continue -> Will skip the current iteration
header = f"""
{10*"="} CONTINUE {"="*10}
"""
print(header)
number = 0
while number < 5:
    number += 1
    if number % 2 == 0:
        continue
    print(f"Number -> {number}")
