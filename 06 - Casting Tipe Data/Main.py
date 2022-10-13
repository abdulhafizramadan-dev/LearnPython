# Casting Tipe Data Python
# Tipe Data: Integer, Float, String, Boolean

# Tipe Data: Integer
print("=====INTEGER=====")
data_int = 10

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)  # Akan false jika integer 0

print("Data :", data_int, "Tipe Data:", type(data_int))
print("Data :", data_float, "Tipe Data:", type(data_float))
print("Data :", data_str, "Tipe Data:", type(data_str))
print("Data :", data_bool, "Tipe Data:", type(data_bool))


# Tipe Data: Float
print("=====FLOAT=====")
data_float = 10.0

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("Data :", data_float, "Tipe Data:", type(data_float))
print("Data :", data_int, "Tipe Data:", type(data_int))
print("Data :", data_str, "Tipe Data:", type(data_str))
print("Data :", data_bool, "Tipe Data:", type(data_bool))


# Tipe Data: String
print("=====STRING=====")
# data_str = "Abdul"
data_str = "10"

data_int = int(data_str)  # Akan error jika nilai str bukan angka
data_float = float(data_str)  # Akan error jika nilai str bukan angka
data_bool = bool(data_str)  # Akan error jika nilai str kosong(empty)

print("Data :", data_str, "Tipe Data:", type(data_str))
print("Data :", data_int, "Tipe Data:", type(data_int))
print("Data :", data_float, "Tipe Data:", type(data_float))
print("Data :", data_bool, "Tipe Data:", type(data_bool))


# Tipe Data: Boolean
print("=====BOOLEAN=====")
data_bool = False

data_int = int(data_bool)  # Akan error jika nilai str bukan angka
data_float = float(data_bool)  # # Akan error jika nilai str bukan angka
data_str = str(data_bool)

print("Data :", data_bool, "Tipe Data:", type(data_bool))
print("Data :", data_int, "Tipe Data:", type(data_int))
print("Data :", data_float, "Tipe Data:", type(data_float))
print("Data :", data_str, "Tipe Data:", type(data_str))
