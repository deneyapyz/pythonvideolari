#fonksiyon tanımlama def fonk_ismi(parametreler):

#geriye değer döndürmeyen:
#geriye değer döndürmeyen fonk. çağırıldığı yerin bir altına döner...
"""
def sehiryaz():
    print("Ankara")
    print("fonksiyon çağırıldı...")
    
for i in range(0,10):
    sehiryaz()
    print("fonksiyondan döngüye dönüldü...")
"""
#geriye değer döndüren ve parametreli:
#geri değer döndüren fonk. çağırıldığı yere -satıra- dönülür...
"""
def topla(a, b):
    toplam = 0
    for i in range(a, b+1):
        toplam+=i
    return toplam

toplamlar = []

for i in range(5):
    print(i+1,". döngü")
    x = int(input("Başlangıç değerini giriniz:"))
    y = int(input("Bitiş değerini giriniz:"))
    toplamlar.append(topla(x,y))

print("Beş döngüdeki her bir toplam:")
print(toplamlar)
"""

"""
def ikinciyiyazdir(*isimler):
    print("Gelen bütün değerler arasındaki ikinci isim "+isimler[1])


ikinciyiyazdir("ahmet","mehmet","utku","gamze","mişa","ayşe","fatma")


def ikinciyiyazdir(**isimler):
    print("Gelen bütün değerler arasındaki istanbuldan gelen "+isimler['istanbul'])


ikinciyiyazdir(isparta="ahmet",ankara="mehmet",istanbul="utku",aydın="gamze",ingiltere="mişa",amerika="ayşe",antalya="fatma")
"""
"""
def pi_yaz(pi=3.14):
    print(pi)

pi_yaz(3)
pi_yaz()
"""

def fonk1():
    print("Fonk. 1 çağırıldı.")
    fonk2()

def fonk2():
    print("Fonk. 2 çağırıldı.")
    arafonk()

def fonk3(a):
    print("Fonk. 3 çağırıldı.")
    return a
    
def arafonk(x=3):
    print("Arafonk. çağırıldı.",str(x))
    print(fonk3(5))
    
fonk1()














