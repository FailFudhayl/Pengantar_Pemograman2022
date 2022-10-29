angka1= int(input("Masukkan angka pertama : "))
angka2= int(input("Masukkan angka kedua : "))
angka3= int(input("Masukkan angka ketiga : "))

if angka1<angka2 and angka1<angka3 :
    angka_terkecil= angka1
elif angka2<angka1 and angka2<angka3 :
    angka_terkecil= angka2
elif angka3<angka1 and angka3<angka2 :
    angka_terkecil= angka3 

for i in range(1, angka_terkecil+1) :
    if angka1%i==0 and angka2%i==0 and angka3%i==0 :
        fpb= i 

print(f"FPB dari {angka1}, {angka2}, dan {angka3} adalah : {fpb}")

