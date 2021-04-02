print("----------HOTEL ASTON----------")
print("Lengkapi Biodata")

nama = input("Masukkan nama anda: ")

print("1. Laki-laki")
print("2. Perempuan")

jenis_kelamin = input("Pilih jenis kelamin anda: ")

if jenis_kelamin == "1":
    print("Selamat datang, Tuan", nama, "!")
elif jenis_kelamin == "2":
    print("Selaamt datang, Nyonya", nama, "!")
else :
    print("Not found")