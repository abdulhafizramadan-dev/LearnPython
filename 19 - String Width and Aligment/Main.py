name = "Abdul Hafiz Ramadan"
age = 19
height = 171.5

# Standard String Alignment
print("\n" + 10*"=" + "String Alignment" + "="*10)
biodata = f"Name = {name}, Age = {age}, Height = {height}"
print(biodata)

# Standard String Multiline
print("\n" + 10*"=" + "String Alignment" + "="*10)
biodata = f"Name = {name}, \nAge = {age}, \nHeight = {height}"
print(biodata)

# String Multiline
print("\n" + 10*"=" + "String Alignment" + "="*10)
biodata = f"""
Name = {name}
Age = {age}
Height = {height}
""".strip()
print(biodata)
