Nim= "H071221026"
a= 2
b= 6
total_detik= ((1000*a)+(100*b)-(10*a))

jam= total_detik//3600
sisa_detik= total_detik%3600
menit= sisa_detik//60
detik= sisa_detik%60

print(jam, 'jam',  menit, 'menit', detik, 'detik')