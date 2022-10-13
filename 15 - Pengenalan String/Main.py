# Pengenalan String

"""
1. Cara pembuatan string
2. Escaping Character
    - \n
    - \t
    - \b
    - \r
    - \r\n
    - \\
3. Raw String
4. Multiline String
5. Multiline Raw String
"""

print()

# Cara membuat string
"""
1. Menggunakan single quote '...'
2. Menggunakan double quote "..."
"""

string_with_single_quote = 'Ini adalah string menggunakan single quote! ("")'
string_with_double_quote = "Ini adalah string menggunakan double quote! ('')"

print(string_with_single_quote)
print(string_with_double_quote)

# Escaping Character (\)

# New line (\n) -> CF line feed -> Unix, MacOs, Linux
print()
print("Ini adalah baris 1\nIni adalah baris 2")

# Tab (\t)
print()
print("Nama\t: Abdul Hafiz Ramadan")
print("Umur\t: 19 Tahun")

# Backspace (\b)
print()
print("Nama \b: Abdul Hafiz Ramadan")

# Remove (\r) -> CR -> carriage return
print()
print("Ini adalah baris 1\rIni adalah baris 2")

# Remove & New Line (\r\n) -> CRLF -> line feed carriage return -> Windows
print()
print("Ini adalah baris 1\r\nIni adalah baris 2")

# Raw String
data_path = r"C:\Users\abdulhafizramadan"
print()
print(data_path)

# Multiline
data_biodata = """
Nama\t: Abdul Hafiz Ramadan
Umur\t: 19 Tahun
Alamat\t: Riau
"""
print(data_biodata)

# Multiline Raw String
data_path = r"""
C:\Users\abdulhafizramadan
"""
print(data_path)
