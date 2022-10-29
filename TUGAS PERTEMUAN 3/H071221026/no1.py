print('MENCARI LUAS BANGUN DATAR')
print('--- PILIH BANGUN DATAR ---')
print('1. Persegi')
print('2. Persegi Panjang')
print('3. Segitiga')
print('4. Jajar Genjang')
print('5. Layang-Layang')

x= int(input('Pilih bangun datar sesuai angkanya : '))

if x==1 :
    sisi_persegi= int(input('sisi = '))
    luas_persegi= sisi_persegi*sisi_persegi
    print('luas persegi = ', luas_persegi)
elif x==2 :
    panjang= int(input('Panjang = '))
    lebar= int(input('Lebar = '))
    luas_persegiPanjang= panjang*lebar
    print('Luas Persegi Panjang = ', luas_persegiPanjang)
elif x==3 :
    alas_segitiga= int(input('alas = '))
    tinggi_segitiga= int(input('tinggi = '))
    luas_segitiga= 0.5*alas_segitiga*tinggi_segitiga
    print('luas segitiga= ', luas_segitiga)
elif x==4 :
    alas_jajarGenjang= int(input('alas = '))
    tinggi_jajarGenjang= int(input('tinggi = '))
    luas_jajarGenjang= alas_jajarGenjang*tinggi_jajarGenjang
    print('Luas Jajar Genjang = ', luas_jajarGenjang)
elif x==5 :
    diagonal01= int(input('diagona 1 = '))
    diagonal02= int(input('diagonal 2 = '))
    luas_layang= 0.5*diagonal01*diagonal02
    print('Luas layang-layang = ', luas_layang)
else :
    print('--- ERORR ---')
    print('Pilih bangun datar sesuai dengan nomor yang tersedia')
