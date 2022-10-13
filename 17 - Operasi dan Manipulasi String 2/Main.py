# Operasi dan Manipulasi String menggunakan Method
"""
1. lowercase
2. uppercase
3. islower
4. isupper
5. istitle
6. startswith
7. endswith
8. join
9. split
10. rjust
11. ljust
12. center
13. strip
"""

fullname = "Abdul Hafiz Ramadan"
print("Your name : " + fullname)

# lower
lower_name = fullname.lower()
print("Lower name : " + lower_name)

# upper
upper_name = fullname.upper()
print("Upper name : " + upper_name)

# islower
print(fullname + " is lower? " + str(fullname.islower()))
print(lower_name + "is lower? " + str(lower_name.islower()))

# isupper
print(fullname + " is upper? " + str(fullname.isupper()))
print(upper_name + " is upper? " + str(upper_name.isupper()))

# istitle
rich_dad_poor_dad = "Rich dad Poor dad"
print(rich_dad_poor_dad + " is title format? " + str(rich_dad_poor_dad.istitle()))
rich_dad_poor_dad_title_format = rich_dad_poor_dad.title()
print(rich_dad_poor_dad_title_format + " is title format? " + str(rich_dad_poor_dad_title_format.istitle()))

# isX cheatsheet
"""
1. isalpha() -> mengecek apakah semua string huruf
2. isalnum() -> mengecek apakah semua string adalah huruf dan angka
3. isdecimal() -> mengecek apakah semua string adalah angka
4. isspace() -> mengecek apakah didalam string terdapat spasi ( ), tab (\t), baris baru (\n)
"""

# startswith
naruto = "Uzumaki Naruto"
print("Apakah " + naruto + ", merupakan clan Uzumaki? " + str(naruto.startswith("Uzumaki")))  # Sensitive Case

# endswith
hotman = "Hotman Paris Harahap"
print("Apakah " + hotman + ", merupakan marga Harahap? " + str(hotman.endswith("Harahap")))  # Sensitive Case

# Join
names = ["Aku", "Suka", "Data"]
print(names)
names_with_space = " ".join(names)
print(names_with_space)

# Split
names_from_cell = "Abdul;Hafiz;Ramadan"
names_in_array = names_from_cell.split(";")
print(names_in_array)

# ljust
name_ljust = "Abdul".ljust(10)
print("|" + name_ljust + "|")

# center
name_center = "Abdul".center(11, "-")
print("|" + name_center + "|")

# rjust
name_rjust = "Abdul".rjust(10)
print("|" + name_rjust + "|")

# Strip
strip_the_string_using_specific_character = name_center.strip("-")
print("|" + strip_the_string_using_specific_character + "|")

strip_the_string_using_space_character = name_rjust.strip()
print("|" + strip_the_string_using_space_character + "|")


