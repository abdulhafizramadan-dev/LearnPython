# 09 - Latihan Perhitungan Sederhana
"""
Konversi Suhu Celcius ke suhu:
- Reamur
- Kelvin
- Fahrenheit
"""

celcius = float(input("Masukan suhu dalam celcius : "))

# Celcius ke Reamur : (4/5) * C
celcius_to_reamur = (4/5) * celcius
print(celcius, "Celcius", "=", celcius_to_reamur, "Reamur")

# Celcius ke Kelvin : C + 273
celcius_to_kelvin = celcius + 273
print(celcius, "Celcius", "=", celcius_to_kelvin, "Kelvin")

# Celcius ke Fahrenheit : ((9/5) * C) + 32
celcius_to_fahrenheit = ((9/5) * celcius) + 32
print(celcius, "Celcius", "=", celcius_to_fahrenheit, "Fahrenheit")
