# Latihan Komparasi dan Logika
# +++++3-------10+++++
input_user = float(input("\nSilakan masukan :\nangka kurang dari 3 atau\nangka lebih dari 10\nmasukan angka :"))

kurangDariTiga = input_user < 3
print(input_user, "kurang dari 3 =", kurangDariTiga)
lebihDariSepuluh = input_user > 10
print(input_user, "lebih dari 10 =", lebihDariSepuluh)

hasil = kurangDariTiga or lebihDariSepuluh
print("Hasil :", hasil)


# -----3++++++10------
input_user = float(input("\nSilakan masukan :\nangka kurang dari 3 dan\nangka lebih dari 10\nmasukan angka :"))

lebihDariTiga = input_user > 3
print(input_user, "lebih dari 3 =", lebihDariTiga)
kurangDariSepuluh = input_user < 10
print(input_user, "kurang dari 10 =", kurangDariSepuluh)

hasil = lebihDariTiga and kurangDariSepuluh
print("Hasil:", hasil)
