# Mengambil input dari user

# Mengambil input string
nama = input("Masukan nama anda: ")

# Mengambil input integer
usia = int(input("Masukan umur anda: "))

# Mengambil input bool
print("\nApakah anda sudah menikah?")
print("0. Belum Menikah")
print("1. Menikah")
status = bool(int(input("masukan jawaban: ")))

print("===== BIODATA =====")
print("Nama anda:", nama)
print("Usia anda:", usia)
print("Sudah menikah?", status)
