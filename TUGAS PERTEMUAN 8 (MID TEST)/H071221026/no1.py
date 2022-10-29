n= int(input("Masukkan n: "))

if n<=0 :
    if n%3 == 0 :
        print(f"{n} berada pada kelompok A1")
    elif n%3 == 1 :
        print(f"{n} berada pada kelompok A2")
    elif n%3 == 2 :
        print(f"{n} berada pada kelompok A3")
elif n>0 and n<=100 :
    if n%3 == 0 :
        print(f"{n} berada pada kelompok B1")
    elif n%3 == 1 :
        print(f"{n} berada pada kelompok B2")
    elif n%3 == 2 :
        print(f"{n} berada pada kelompok B3")
elif n>100 and n<=200 :
    if n%3 == 0 :
        print(f"{n} berada pada kelompok C1")
    elif n%3 == 1 :
        print(f"{n} berada pada kelompok C2")
    elif n%3 == 2 :
        print(f"{n} berada pada kelompok C3")
elif n>200 :
    if n%3 == 0 :
        print(f"{n} berada pada kelompok D1")
    elif n%3 == 1 :
        print(f"{n} berada pada kelompok D2")
    elif n%3 == 2 :
        print(f"{n} berada pada kelompok D3")