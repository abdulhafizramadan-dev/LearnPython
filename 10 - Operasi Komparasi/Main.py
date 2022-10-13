# Operasi Komparasi
"""
1. <
2. >
3. <=
4. >=
5. ==
6. !=
7. is
8. is not
"""

a = 4
b = 2

# Operasi lebih kecil dari (<)
print("\n====== Lebih kecil dari (<) ======\n")
hasil = a < b
print(a, "<", b, "=", hasil)
hasil = b < a
print(b, "<", a, "=", hasil)

# Operasi lebih besar dari (>)
print("\n====== Lebih besar dari (>) ======\n")
hasil = a > b
print(a, ">", b, "=", hasil)
hasil = b > a
print(b, ">", a, "=", hasil)

# Operasi lebih kecil dari sama dengan (<=)
print("\n====== Lebih sama dengan (=<) ======\n")
hasil = a <= b
print(a, "<=", b, "=", hasil)
hasil = b <= a
print(b, "<=", a, "=", hasil)
hasil = a <= 4
print(a, "<=", 4, "=", hasil)

# Operasi lebih besar dari sama dengan (>=)
print("\n====== Lebih besar sama dengan (>=) ======\n")
hasil = a >= b
print(a, ">=", b, "=", hasil)
hasil = b >= a
print(b, ">=", a, "=", hasil)
hasil = a >= 4
print(a, ">=", 4, "=", hasil)

# Operasi sama dengan (==)
print("\n====== Sama dengan (==) ======\n")
hasil = a == b
print(a, "==", b, "=", hasil)
hasil = a == a
print(a, "==", a, "=", hasil)

# Operasi tidak sama dengan (!=)
print("\n====== Tidak sama dengan (!=) ======\n")
hasil = a != b
print(a, "!=", b, "=", hasil)
hasil = a != a
print(a, "!=", a, "=", hasil)

c = 4

# Operasi is (is)
print("\n====== Is ======\n")
hasil = a is b
print(a, "is", b, "=", hasil)
hasil = a is a
print(a, "is", a, "=", hasil)
hasil = a is c
print(a, "is", c, "=", hasil)

# Operasi is not (is not)
print("\n====== Is Not ======\n")
hasil = a is not b
print(a, "is not", b, "=", hasil)
hasil = a is not a
print(a, "is not", a, "=", hasil)
hasil = a is not c
print(a, "is not", c, "=", hasil)
