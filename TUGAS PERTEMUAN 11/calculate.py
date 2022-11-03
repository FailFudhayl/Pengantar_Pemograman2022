angka_1 = float(input("masukkan angka pertama = "))
print("Pilih Operator")
print("+")
print("-")
print("X")
print("/")
operator = input("Masukkan Operastor : ")
angka_2 = float(input("masukkan angka kedua = "))

if operator == "+":
    hasil = angka_1 + angka_2
    print (f"Hasilnnya Adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print (f"Hasilnnya Adalah {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print (f"Hasilnnya Adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print (f"Hasilnnya Adalah {hasil}")
else:
    print("Silah masukkan format yang benar!")