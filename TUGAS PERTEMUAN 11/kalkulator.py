jumlah_angka= int(input("Masukkan Jumlah Angka : "))
Numbers= []
for j in range(jumlah_angka) :
    angka= int(input("Masukkan angka : "))
    Numbers.append(angka)
print("Pilih Operasi")
print("+")
print("-")
print("X")
print("/")
operasi= input("Pilih Operasi : ")
if operasi== "+" :
    jumlah=0
    for i in Numbers :
        jumlah+=i
    print(jumlah)
elif operasi== "-" :
    jumlah= 0
    for i in Numbers :
        jumlah-=i
    print(jumlah*(-1))
elif operasi== "X" :
    jumlah= 1
    for i in Numbers :
        jumlah*=i 
    print(jumlah)
elif operasi== "/" :
    jumlah= 1
    for i in Numbers :
        jumlah/=i
    print(jumlah)
else :
    print("Pilih Operasi yang benar")