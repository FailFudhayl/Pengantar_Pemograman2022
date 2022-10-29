try :  
    print('==== MASUKKAN 2 ANGKA ===')
    nilai_awal= int(input('AWAL : '))
    nilai_akhir= int(input('AKHIR : '))

    for i in range(nilai_awal,nilai_akhir+1) :
        if nilai_awal<0 and nilai_awal%2==1 :
            print(nilai_awal, 'ganjil negatif')
        elif nilai_awal<0 and nilai_awal%2==0 :
            print(nilai_awal, 'genap negatif')
        elif nilai_awal>0 and nilai_awal%2==1 :
            print(nilai_awal, 'ganjil positif')
        elif nilai_awal>0 and nilai_awal%2==0 :
            print(nilai_awal, 'genap positif')
        elif nilai_awal==0 :
            print(nilai_awal, 'nol')
        elif nilai_akhir<0 and nilai_akhir%2==1 :
            print(nilai_akhir, 'ganjil negatif')
        elif nilai_akhir<0 and nilai_akhir%2==0 :
            print(nilai_akhir, 'genap negatif')
        elif nilai_akhir>0 and nilai_akhir%2==1 :
            print(nilai_akhir, 'ganjil positif')
        elif nilai_akhir>0 and nilai_akhir%2==0 :
            print(nilai_akhir, 'genap positif')
        elif nilai_akhir==0 :
            print(nilai_akhir, 'nol')
        
        if nilai_awal>nilai_akhir :
            nilai_awal-=1
        elif nilai_awal<nilai_akhir :
            nilai_awal+=1
except :
    print('ERROR, TOLONG MASUKKAN NILAI DALAM BENTUK ANGKA')        
