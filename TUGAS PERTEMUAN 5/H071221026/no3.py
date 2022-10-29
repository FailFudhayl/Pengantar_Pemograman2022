string= input("masukkan string utama : ")
substring= input("masukkan substring : ")
string_setengah= int(len(string)/2)
if len(string)%2 == 0 :
    print(string[:string_setengah]+substring+string[string_setengah:])
else :
    print('operasi tidak dapat dilakukan')