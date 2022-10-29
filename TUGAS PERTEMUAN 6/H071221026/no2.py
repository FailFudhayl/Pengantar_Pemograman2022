daftar_nilai= [87, 80, 67, 88, 98, 73, 81]

a= int(input("Masukkan nilai A : "))
k= int(input("Masukkan nilai K : "))

for i in range (a, k) :
    input_newElement= int(input(f"Masukkan nilai baru dari Indeks ke {i} : "))
    daftar_nilai[i]= input_newElement

print(f"Daftar nilai yang telah diubah : {daftar_nilai}")