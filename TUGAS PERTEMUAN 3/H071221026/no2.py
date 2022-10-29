try :  
    x= int(input('Masukkan Koordinat X : '))
    y= int(input('Masukkan Koordinat Y : '))
    if x>0 and y>0 :
        print('Koordinat :', '('+str(x)+','+str(y)+')', 'berada pada kuadran 1')
    elif x<0 and y>0 :
        print('Koordinat :', '('+str(x)+','+str(y)+')', 'berada pada kuadran 2')
    elif x<0 and y<0 :
        print('Koordinat :', '('+str(x)+','+str(y)+')', 'berada pada kuadran 3')
    elif x>0 and y<0 :
        print('Koordinat :', '('+str(x)+','+str(y)+')', 'berada pada kuadran 4')
    elif x>0 or x<0 and y==0 :
        print('Koordinat :', '('+str(x)+','+str(y)+')', 'berada pada garis X')
    elif y>0 or y<0 and x==0 :
        print('Koordinat :', '('+str(x)+','+str(y)+')', 'berada pada garis Y')
    else :
        print('Koordinat ; (0,0), berada pada pusat koordinat')
except :
    print('ERROR, Program Hanya Menerima Masukan Angka')
