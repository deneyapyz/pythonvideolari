import matplotlib.pyplot as p
"""
p.plot([45, 78, -90, 57, 145])
p.xlabel('zamana göre akış')
p.ylabel('ölçülen değerler')
p.show()

p.plot([2, 4, 6, 8, 10], [100, 180, 390, -100, 500], 'r--')
p.xlabel('zamana göre akış')
p.ylabel('ölçülen değerler')
p.show()
"""
deger_gruplari = ['birinci', 'ikinci', 'ucuncu', 'dorduncu']
veriler = [23, 67, 89, 67]

p.figure(figsize=(9,3))
p.subplot(131)
p.bar(deger_gruplari, veriler)
#p.show()
p.subplot(132)
p.plot(deger_gruplari, veriler)
#p.show()
p.subplot(133)
p.scatter(deger_gruplari, veriler)
p.show()

import numpy as np

def fonksiyon_sin(x):
    return np.sin(x)

def fonksiyon_cos(x):
    return np.cos(x)

degerler = np.arange(75.5, 110.5, 0.1)

p.figure()
p.subplot(211)
p.plot(degerler, fonksiyon_sin(degerler), 'r--')
p.subplot(212)
p.plot(degerler, fonksiyon_cos(degerler), 'b*')
p.suptitle('Sin ve Cos göre genel zaman serileri')
p.show()

degerler_pasta = np.array([45, 67, 89, 90])
etiketler = ['opel', 'fiat', 'ford', 'audi']
p.pie(degerler_pasta, labels = etiketler, colors = ['r', 'b', 'k', 'm'])
p.legend()
p.show()

