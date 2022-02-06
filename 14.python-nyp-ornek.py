import python_nyp_sinif as s
#from python_nyp_sinif import Tasitlar

x = Insan()
x.isim = "ahmet"
x.boy = 181
x.kilo = 76
x.goz_rengi = "ela"
x.sac_rengi = "siyah"
x.hiz = 10

y = Insan()
y.isim = "mehmet"
y.boy = 205
y.kilo = 80
y.goz_rengi = "mavi"
y.sac_rengi = "sarı"
y.hiz = 15

print(x.isim, y.isim)
x.kos()
y.kos()
print(x.el_sayisi, y.el_sayisi)

