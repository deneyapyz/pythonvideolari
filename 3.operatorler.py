"""
Operatörler
1- Atama operatörü / operatörleri
2- Aritmetiksel operatörler
3- Karşılaştırma operatörleri
4- Mantıksal operatörler
"""
x = 5 
y = x + 5 #10
#aritmetik operatörler --> +, -, /, *, //, %, **

z = y - 4 #6

a = z / 3

b = a * 3

c = b / 4
d = b // 4

print(x,y,z,a,b,c,d)

mod1 = z % 3
mod2 = z % 4

us1 = 3 ** 2
us2 = mod2 ** 5

print(mod1, mod2, us1, us2)

###

sayi1 = 5
sayi2 = 7
sayi1 += sayi2 #sayi1 = sayi1 + sayi2
print(sayi1)

sayi3 = 10
sayi4 = 5
#sayi3 -= sayi4 #sayi3 = sayi3 - sayi4
#sayi3 *= sayi4 #sayi3 = sayi3 - sayi4
sayi3 **= sayi4 #sayi3 = sayi3 - sayi4
#sayi3 /= sayi4 #sayi3 = sayi3 / sayi4
#sayi3 //= sayi4 #sayi3 = sayi3 / sayi4
#sayi3 %= sayi4 #sayi3 = sayi3 / sayi4
print(sayi3)

#Karşılaştırma operatörleri --> ==, !=, <, >, <=, >=
if (2==2):
    print("Eşitlik var!")

if (2!=4):
    print("İki sayı birbirinden farklı!")
    
if (2>4):
    print("İki dörtten büyüktür...")

if (2>1):
    print("İki birden büyüktür...")
"""
if (2>=1):
    print("Soldaki sayı sağdaki sayıya eşit veya sağdaki sayıdan büyüktür...")
"""
if (2>=2):
    print("Soldaki sayı sağdaki sayıya eşit veya sağdaki sayıdan büyüktür...")
    
"""
Mantıksal operatörler
and --> Bütün durumlar 1 ise sonuç 1 aksi halde sonuç 0
or --> Bütün durumlar 0 ise sonuç 0 aksi halde sonuç 1
not --> Bir mantıksal ifadeyi tersine göre düşünür (1'i 0 olarak, 0'ı 1 olarak)
"""

yas = 10

if (yas >= 10) and (yas < 25):  #10<=yas<25 [10,25)
    print("Bu yaştaki kişi oldukça genç-1")

if (yas >= 10) or (yas > 50):  #10<=yas   yas>50 
    print("Bu yaştaki kişi oldukça genç-2")
    
kilo = 75

if (yas >= 10) and (yas < 25) and (kilo < 90) and (kilo == 50):  
    print("Bu kişi oldukça genç ve kilosu da çok değil-1")

if (yas >= 10) and (yas < 25) and (kilo < 90) or (kilo == 50):  
    print("Bu kişi oldukça genç ve kilosu da çok değil-2")

if (yas >= 10) and (yas < 25) and (kilo < 90) and not(kilo == 50):  
    print("Bu kişi oldukça genç ve kilosu da çok değil-3")

