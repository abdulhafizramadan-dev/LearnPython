# Homework

"""
Konversi dari :
- Fahrenheit ke Kelvin
- Kelvin ke Fahrenheit
"""

# Fahrenheit ke Kelvin
# (((5/9) * F) - 32) + 273
# fahrenheit = float(input("Masukan nilai fahrenheit : "))
# fahrenheit_to_kelvin = (((5/9) * fahrenheit) - 32) + 273
# print(fahrenheit, "Fahrenheit", "=", fahrenheit_to_kelvin, "Kelvin")

# Kelvin ke Fahrenheit
# Kelvin ke Celcius
# (K-273)
# Celcius ke Fahrenheit
# ((9/5) * C) + 32
kelvin = float(input("Masukan nilai kelvin : "))
kelvin_to_celcius = kelvin - 273
kelvin_to_fahrenheit = ((9/5) * kelvin_to_celcius) + 32
print(kelvin, "Celcius", "=", kelvin_to_fahrenheit, "Fahrenheit")
