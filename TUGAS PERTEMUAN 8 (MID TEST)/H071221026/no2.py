try :
    x= int(input("Masukkan X : "))
    y= int(input("Masukkan Y : "))
except :
    print("Masukkan angka sebagai inputan")

if x>0 :
    if y>0 :
        print(f"Koordinat : ({x},{y}) berada pada kuadran 1")
    elif y<0 :
        print(f"Koordinat : ({x},{y}) berada pada kuadran 4")
elif x<0 :
    if y>0 :
        print(f"Koordinat : ({x},{y}) berada pada kuadran 2")
    elif y<0 :
        print(f"Koordinat : ({x},{y}) berada pada kuadran 3")
elif x==0 and y==0 :
    print(f"Koordinat : ({x},{y}) berada pada pusat koordinat") 
elif x==0 :
    print(f"Koordinat : ({x},{y}) berada pada garis Y")
elif y==0 :
    print(f"Koordinat : ({x},{y}) berada pada garis X")
else :
    print(f"Koordinat : ({x},{y}) berada pada garis X")