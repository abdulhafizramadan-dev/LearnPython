# Operator Bitwise
"""
1. OR (|)
2. AND (&)
3. XOR (^)
4. NOT (~)
5. Shift Right (>>)
6. Shift Left (<<)
"""

print("")
print(8*"=", "OPERATOR BITWISE", 8*"=")

a = 9
b = 5

# OR (|)
"""
9 = 00001001
5 = 00000101
------------ (|)
    00001101 (13)
"""
print("")
print(16*"=", "|", 16*"=")
c = a | b
print("Nilai a =", a, ", nilai biner =", format(a, "08b"))
print("Nilai b =", b, ", nilai biner =", format(a, "08b"))

print(a, "\t:", format(a, "08b"))
print(b, "\t:", format(b, "08b"))
print(16*"-", "(|)")
print(c, "\t:", format(c, "08b"))


# AND (&)
"""
9 = 00001001
5 = 00000101
------------ (|)
    00000001 (1)
"""
print("")
print(16*"=", "&", 16*"=")
c = a & b
print("Nilai a =", a, ", nilai biner =", format(a, "08b"))
print("Nilai b =", b, ", nilai biner =", format(a, "08b"))

print(a, "\t:", format(a, "08b"))
print(b, "\t:", format(b, "08b"))
print(16*"-", "(&)")
print(c, "\t:", format(c, "08b"))


# XOR (^)
"""
9 = 00001001
5 = 00000101
------------ (^)
    00001100 (12)
"""
print("")
print(16*"=", "^", 16*"=")
c = a ^ b
print("Nilai a =", a, ", nilai biner =", format(a, "08b"))
print("Nilai b =", b, ", nilai biner =", format(a, "08b"))

print(a, "\t:", format(a, "08b"))
print(b, "\t:", format(b, "08b"))
print(16*"-", "(^)")
print(c, "\t:", format(c, "08b"))

# NOT (~)
"""
9   = 00001001
-------------- (~)
      -0001010 (-10)
"""
print("")
print(16*"=", "~", 16*"=")
c = ~a
print("Nilai a =", a, ", nilai biner =", format(a, "08b"))

print(16*"-", "(~)")
print(c, "\t:", format(c, "08b"))

print("")
print(16*"=", "^", 16*"=")
d = ~b
print("Nilai a =", b, ", nilai biner =", format(b, "08b"))

print(16*"-", "(~)")
print(d, "\t\t:", format(d, "08b"))


# Shift Right (>>)
"""
9   = 00001001
-------------- (>> 1)
      -0000100 (-10)
"""
print("")
print(16*"=", ">>", 16*"=")
c = a >> 1
print("Nilai a =", a, ", nilai biner =", format(a, "08b"))

print(16*"-", "(>> 1)")
print(c, "\t:", format(c, "08b"))

print("")
print(16*"=", "^", 16*"=")
d = b >> 1
print("Nilai a =", b, ", nilai biner =", format(b, "08b"))

print(16*"-", "(>> 1)")
print(d, "\t\t:", format(d, "08b"))


# Shift Right (>>)
"""
9   = 00001001
-------------- (>> 1)
      -0000100 (-10)
"""
print("")
print(16*"=", ">>", 16*"=")
c = a >> 1
print("Nilai a =", a, ", nilai biner =", format(a, "08b"))

print(16*"-", "(>> 1)")
print(c, "\t:", format(c, "08b"))

print("")
print(16*"=", "^", 16*"=")
d = b >> 1
print("Nilai a =", b, ", nilai biner =", format(b, "08b"))

print(16*"-", "(>> 1)")
print(d, "\t\t:", format(d, "08b"))
