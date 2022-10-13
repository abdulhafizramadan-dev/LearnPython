header = f"""
{10*"="} KALKULATOR SEDERHANA {"="*10}
"""

print(header)

operand1 = float(input("Masukan angka 1 = "))
operator = input("Masukan operator (+, -, x, /) = ")
operand2 = float(input("Masukan angka 2 = "))

print()

if operator == "+":
    result = operand1 + operand2
    print(f"Hasil kalkulator = {result}")
elif operator == "-":
    result = operand1 - operand2
    print(f"Hasil kalkulator = {result}")
elif operator == "x" or operator == "*":
    result = operand1 * operand2
    print(f"Hasil kalkulator = {result}")
elif operator == "/":
    result = operand1 / operand2
    print(f"Hasil kalkulator = {result}")
else:
    print("Masukin operator yang bener dong!")
