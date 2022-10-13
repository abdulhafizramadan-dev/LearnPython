"""
## Format String
1. String
2. Int
3. Decimal
4. Boolean
5. Number Formatting
6. Decimal Formatting
7. Decimal Formatting - Leading Zero
8. Show Minus
9. Show Plus
10. Percent Formatting
11. Expression
12. Binary
13. Octal
14. Hexadecimal
"""

# Manual String Concatenation
first_name = "Abdul"
middle_name = "Hafiz"
last_name = "Ramadan"

full_name = first_name + " " + middle_name + " " + last_name
print(full_name)

# By default, adding new space in the end of the word
print(first_name, middle_name, last_name)


# Using String Formatting
name = "Abdul Hafiz Ramadan"
say_hello = f"Hello {name}"
print(say_hello)

# Int Formatting
name = "Abdul Hafiz Ramadan"
age = 19
salary = 50_000
introduce_myself = f"Hello my name is {name}, and my age is {age}. and my salary is > ${salary:,}"
print(introduce_myself)

# Decimal Formatting
my_decimal_number = 100.0000
format_decimal = f"The actual decimal number = {my_decimal_number}"
print(format_decimal)

# Format the length of number behind the comma
format_decimal = f"The actual decimal number = {my_decimal_number:.3f}"
print(format_decimal)

# Format the length of number front the comma
format_decimal = f"The actual decimal number = {my_decimal_number:10.3f}"
print(format_decimal)
# Adding leading zero
format_decimal = f"The actual decimal number = {my_decimal_number:010.3f}"
print(format_decimal)

# Show Minus
negative_number = -100
format_minus = f"Example of negative number : {negative_number}"
print(format_minus)

# Show Positive (Default not shown)
positive_number = 100
format_positive = f"Example of positive number : {positive_number}"
print(format_positive)
format_positive = f"Example of positive number : {positive_number:+d}"
print(format_positive)

# Percent Formatting
percent = 0.0540
format_percent = f"Example of percent (Not Formatted) : {percent}"
print(format_percent)
format_percent = f"Example of percent : {percent:.2%}"
print(format_percent)

# Expression
apple_price = 10_000
apple_quantity = 10
format_expression = f"The price of apple is ${apple_price}, and the quantity is {apple_quantity:,} total = ${apple_price*apple_quantity:,}"
print(format_expression)


number = 100

# Binary
format_binary = f"{number} in binary = {bin(number)}"
print(format_binary)

# Octal
format_octal = f"{number} in octal = {oct(number)}"
print(format_octal)

# Hexadecimal
format_hex = f"{number} in hexadecimal = {hex(number)}"

