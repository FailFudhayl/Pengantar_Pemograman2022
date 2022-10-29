list= []

panjang_list= int(input('Masukkan Panjang List : '))

for i in range(1, panjang_list+1) :
    masukkan_elemen= int(input(f"Masukkan elemen ke-{i} : "))
    list.append(masukkan_elemen)

angka_terbesar= list[0]
angka_terkecil= list[0]

for elm in list :
    if elm>angka_terbesar :
        angka_terbesar=elm

for elmns in list :
    if elmns<angka_terkecil :
        angka_terkecil=elmns

jumlah= sum(list)
print(f"Elemen terbesar : {angka_terbesar}")
print(f"Elemen terkecil : {angka_terkecil}")
print(f"Penjumlahan semua elemen : {jumlah}")