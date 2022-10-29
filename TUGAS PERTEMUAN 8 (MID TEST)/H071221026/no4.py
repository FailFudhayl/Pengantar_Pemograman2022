panjang= int(input("Masukkan panjang kotak : "))
lebar= int(input("Masukkan lebar kotak : "))

print('#'*panjang)
for i in range(1, panjang-1) :
    print('#'+(' '*(panjang-2))+'#')
print('#'*panjang)