# Operasi dan Manipulasi String

"""
1. Concatenation (+)
2. Length (len)
3. Contain (in)
4. Contain Not (not in)
5. Looping (int*str)
6. Indexing ([index])
7. min
8. max
9. method
10. ord
11. chr
12. method count()
"""

# Concatenation
print()
first_name = "Abdul"
mid_name = "Hafiz"
last_name = "Ramadan"

age = 19

full_name = first_name + " " + mid_name + " " + last_name
print(full_name)

# error_concatenation = "Nama saya " + first_name + ", dan umur saya " + age + " tahun!" # Error

# Length
panjang_fullname = len(full_name)
print(full_name + " memiliki panjang = " + str(panjang_fullname))

# Contain
username = "@abdulhafizramadan"
is_instagram_username = "@" in username
print(username + " apakah merupakan username instagram? " + str(is_instagram_username))

# Contain Not
is_not_instagram_username = "@" not in username
print(username + " apakah bukan merupakan username instagram? " + str(is_not_instagram_username))

# Looping
header = 9*"==|" + " TITLE HERE " + "|=="*9
print(header)

# Indexing
print("Index ke 0 dari fullname = " + full_name[0])
print("Index ke 6 dari fullname = " + full_name[6])
print("Index ke -1 dari fullname = " + full_name[-1])
print("Index ke 0:6 " + full_name[0:7])
print("Index ke [0,2,4,6,8] dari fullname = " + full_name[0:9:2])

# Min
min_character_of_fullname = min(full_name)
print("Min character of " + full_name + ", " + min_character_of_fullname)

# Ord
ascii_code_of_spaci = ord(" ")
print("Ascii code dari spasi " + str(ascii_code_of_spaci))

