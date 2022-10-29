def dollar_coversion(dollar) :
    if dollar>0 :
        print(f'konversi {dollar}$ ke rupiah: {dollar*14953}')
    else :
        print('inputan tidak boleh negatif')

dollar= float(input("Input uang dollar untuk dikonversi ke rupiah : "))
dollar_coversion(dollar)
