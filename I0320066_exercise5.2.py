#Penggunaan if untuk dua kasus

#Inputkan bilangan
bilangan = int(input("Masukkan bilangan bulat: "))

#Memeriksa bilangan
if bilangan % 2 == 0 :
    print("%d adalah bilangan genap " % bilangan)
else :
    print("%d adalah bilangan ganjil " % bilangan)
print()