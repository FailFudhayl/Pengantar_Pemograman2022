list5= list(map(int, input("Masukkan list n : ").split(" ")))
try : 
    listA= []
    for i in list5[0:4] :
        listA.append(i)
    listB= []
    for i in list5[1:4+1] :
        listB.append(i)

    print(f'penjumlahan minimum : {sum(listA)}')
    print(f'penjumlahan maksimum : {sum(listB)}')
except :
    print("panjang list tidak sama dengan 5")

