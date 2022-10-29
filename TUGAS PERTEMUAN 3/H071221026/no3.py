try :
    x= int(input('Masukkan nilai X : '))
    if x>=1 :
        for i in range (0,x) :
            print('Akar Kuadrat dari', x, 'adalah', x**0.5)
            x-=1

    else :
        for j in range (x,2) :
            print('Akar Kuadrat dari', x, 'adalah', x**0.5)
            x+=1
except :
    print('ERROR, TOLONG MASUKKAN NILAI DALAM BENTUK ANGKA')