import datetime

banner_format = f"""
{10*"="} KALKULATOR UMUR {"="*10}
Silahkan masukan tanggal, bulan dan tahun lahir!
"""

print(banner_format)

input_date = int(input("Masukan tanggal lahir : "))
input_month = int(input("Masukan bulan lahir  : "))
input_year = int(input("Masukan tahun lahir : "))

current_date = datetime.date.today()
birth_date = datetime.date(input_year, input_month, input_date)

print(f"Hari ini tanggal : {current_date}")

birth_in_date = current_date - birth_date
birth_year = birth_in_date.days // 365
birth_month = (birth_in_date.days % 365) // 30
birth_date = (birth_in_date.days % 365) % 30

print(f"Umur anda adalah {birth_year} tahun, {birth_month} bulan dan {birth_date} hari")

