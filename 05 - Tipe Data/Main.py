# Integer Type
from ctypes import c_double

data_integer = 1000
print("Data =", data_integer, "Type of data =", type(data_integer))

# Float Type
data_float = 100.0
print("Data =", data_float, "Type of data =", type(data_float))

# String Type
data_string = "Abdul"
print("Data =", data_string, "Type of data =", type(data_string))

# Boolean Type
data_boolean = True
print("Data =", data_boolean, "Type of data =", type(data_boolean))

# Complex Type
data_complex = complex(10, 5)
print("Data =", data_complex, "Type of data =", type(data_complex))

# C Types
data_c_double = c_double(100.0)
print("Data =", data_c_double, "Type of data =", type(data_c_double))
