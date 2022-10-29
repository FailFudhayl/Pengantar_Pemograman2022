mySet= set()
while True :
    print("Pilih Opsi: ")
    print("1. Masukkan satu data ke set xyz")
    print("2. Masukkan lebih dari satu data ke set xyz")
    print("3. Hapus satu data dari set xyz")
    print("4. Hapus semua elemen set xyz")
    print("5. Keluar dari program")
    print("")
    print(f"set xyz sekarang: {mySet}")
    print("")
    try :
        permintaan= int(input("Masukkan Opsi >> "))
        if permintaan==5 :
            print("keluar dari program....")
            break
        elif (permintaan<=0) or (permintaan>5):
            print("Inputan opsi salah")
        elif permintaan==1 :
            mySet.add(int(input("Masukkan satu data baru >> ")))
        elif permintaan==2 :
            mySet.update(map(int, input("Masukkan satu data baru : ").split(' ')))
        elif permintaan==3 :
            mySet.remove(int(input("Masukkan satu data yang ingin dihapus >> ")))
        elif permintaan==4 :
            mySet.clear()
            print("menghapus semua data...")
    except :
        print("Inputan opsi salah")