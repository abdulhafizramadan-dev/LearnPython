"""
+
++
+++
++++
+++++
"""
# Using For
print("""
Using For
""")
row = 5
column = 1
for item in range(row):
    print("+"*column)
    column += 1

# Using While
print("""
Using While
""")
row = 5
column = 1
while column <= row:
    print("+"*column)
    column += 1


"""
*
***
*****
*******
"""
# Using For
print("""
Using For
""")
row = 7
for i in range(1, 7+1):
    if not i % 2:
        continue
    print(i*"+")


print("""
Using While
""")
row = 7
column = 1
temp = 0
while temp < 7:
    if column % 2:
        print(column * "+")
    column += 1
    temp += 1


"""
   *
  ***
 *****
*******
"""


