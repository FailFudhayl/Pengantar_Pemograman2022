print('---Menentukan FPB---')
try :
    def menentukan_fpb(a, b) :
        if a>b :
            bilangan_terkecil= b
        elif b>a :
            bilangan_terkecil= a
        else :
            bilangan_terkecil= a or b
        for i in range(1, bilangan_terkecil+1) :
            if (a%i==0) and (b%i==0) :
                fpb=i
        return fpb

    a= int(input("Masukkan bilangan a : "))
    b= int(input("Masukkan bilangan b : "))

    print(f"FPB dari {a} dan {b} = {menentukan_fpb(a,b)}")

except :
    print('Input hanya terdiri dari angka')