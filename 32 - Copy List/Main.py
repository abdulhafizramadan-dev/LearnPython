names = ["Abdul", "Hafiz", "Ramadan"]
names2 = names

print(f"Names  = {names}")
print(f"Names2 = {names2}")

names[1] = "Muslim"
print()

print(f"Names  = {names}")
print(f"Names2 = {names2}")

print()

print(f"Memory address Names  = {hex(id(names))}")
print(f"Memory address Names2 = {hex(id(names2))}")

"""
That way when we update the names, names2 will be changed to. 
Because both of names and names2 have the same object reference in memory.
To solve this problem we will create the copy of names using copy() method, as shown below
"""

names3 = names.copy()
print()

print(f"Names  = {names}")
print(f"Names2 = {names2}")
print(f"Names3 = {names3}")

names[2] = "Ridho"
print()

print(f"Names  = {names}")
print(f"Names2 = {names2}")
print(f"Names3 = {names3}")


names3[0] = "Ridho"
print()

print(f"Names  = {names}")
print(f"Names2 = {names2}")
print(f"Names3 = {names3}")

print()

print(f"Memory address of names  = {hex(id(names))}")
print(f"Memory address of names2 = {hex(id(names2))}")
print(f"Memory address of names3 = {hex(id(names3))}")

