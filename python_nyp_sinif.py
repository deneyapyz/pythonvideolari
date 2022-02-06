class Insan:
    el_sayisi = 0
    isim = ""
    boy = 0
    kilo = 0
    goz_rengi = ""
    sac_rengi = ""
    hiz = 0
    
    def __init__(self):
        self.el_sayisi = 2
        
    def kos(self):
        print(self.isim,str(self.hiz),"değerinde hız ile koşuyor")
        
class Tasitlar:
    pass
"""
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
"""