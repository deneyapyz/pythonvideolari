#python library çağrısı: import küt.adı
#import math as matematik
#print(matematik.pi)

#spesifik kütüphane modülünü - bileşenini çağırmak için:
#from math import pi
#print(pi)

"""
from math import *
print(pi)
print(cos(90))

import array as dizi
"""

#numpy kütüphanesi
import numpy as np
dizi = np.array([3, 7, 9, 12, 90, -1, 45, 7])
print(dizi)
print(dizi.ndim)
print(dizi.shape)
dizi2 = dizi.reshape(2,4)
print(dizi2)

dizi3 = np.arange(0,10,2)

dizi4 = dizi.reshape(4,2)
print(dizi4[0])
print(dizi4[0:2])
print(dizi4[:,1])
print(dizi4[2,:])

dizi5 = np.zeros((6,10))

dizi6 = np.ones((6,10))

dizi7 = np.eye(5)

dizi_butun_satir = np.concatenate([dizi5, dizi6], axis=0)

dizi_butun_sutun = np.concatenate([dizi5, dizi6], axis=1)

print(dizi4.max())
print(dizi4.min())
print(dizi4.mean())
print(dizi4.sum())
print(dizi4.sum(axis=0))
print(dizi4.sum(axis=1))

print(np.median(dizi4))
print(np.var(dizi4))
print(np.std(dizi4))

dizi8 = np.ones((4,2))
print(dizi4 + dizi8)
print(dizi4 - dizi8)
print(dizi4 * dizi8)
print(dizi4 + 10)
print(dizi4 * 56)

#diğer fonk. np.log, np.exp, np.cos...vs.

yeni_dizi = np.dot(dizi4,dizi2)
print(dizi4.T)

sonuc = yeni_dizi >= 500
print(sonuc)












