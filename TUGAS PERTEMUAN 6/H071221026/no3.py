n= int(input("jumlah baris dan kolom : "))
list=[[int(input(f"masukkaan baris {j} dan kolom {i} : ")) for i in range(1,n+1)] for j in range(1,n+1)]

diagonal1= []
for k in range(0,n) :
    penjumlahan= list[k][k]
    diagonal1.append(penjumlahan)

list.reverse()
diagonal2= []
for h in range(0,n) :
    penjumlahan= list[h][h]
    diagonal2.append(penjumlahan)

print(f"selisih diagoanl = {(sum(l for l in diagonal2))-(sum(l for l in diagonal1))}")