print('Selamat datang untuk memulai input data anda')
nama = input('Input nama: ')
umur = int(input('Input umur: '))
alamat = input('Input alamat: ')

dict_profile = {
    'nama' : nama,
    'umur' : umur,
    'alamat' : alamat
    }

while True :
    print('='*60)
    print(f"Selamat datang {dict_profile['nama']}, silahkan pilih opsi")
    print('='*60)
    print('1. Detail anda')
    print('2. Ubah nama')
    print('3. Ubah umur')
    print('4. Ubah alamt')
    print('5. Keluar')
    print('='*60)
    try :
        opsi = int(input('Input opsi: '))
    except :
        print('Opsi salah')
    print('='*60)
    if opsi<=0 or opsi>5 :
        print('Opsi salah')
    elif opsi==1 :
        print('Data anda adalah')
        print(f"Nama : {dict_profile.get('nama')}")
        print(f"Umur : {dict_profile.get('umur')}")
        print(f"Alamat : {dict_profile.get('alamat')}")
    elif opsi==2 :
        rename = input('Silahkan input nama baru: ')
        dict_profile['nama']=rename
        print('Data anda sukses diper barui')
    elif opsi==3 :
        reage = input('Silahkan input umur baru: ')
        dict_profile['umur']=reage
        print('Data anda sukses diper barui')
    elif opsi==4 :
        readress = input('Silahkan input umur baru: ')
        dict_profile['alamat']=readress
        print('Data anda sukses diper barui')
    elif opsi==5 :
        print(f'Selamat tinggal {dict_profile["nama"]}')
        break
