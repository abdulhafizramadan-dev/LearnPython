# Operator Logika atau Boolean
"""
1. NOT
2. OR
3. AND
4. XOR
"""

# NOT (Membalik nilai operand)
print("\n====== NOT ======\n")
a = False
b = not a
print("Nilai a=", a)
print("Nilai b=", b)


# OR (Akan true jika salah satu/kedua operan bernilai true)
print("\n====== OR ======\n")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)
a = True
b = True
c = a or b
print(a, "OR", b, "=", c)


# AND (Akan true jika kedua operan bernilai true)
print("\n====== AND ======\n")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)
a = True
b = False
c = a and b
print(a, "AND", b, "=", c)
a = False
b = True
c = a and b
print(a, "AND", b, "=", c)
a = True
b = True
c = a and b
print(a, "AND", b, "=", c)


# AND (Akan true jika kedua operan bernilai true)
print("\n====== XOR ======\n")
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
