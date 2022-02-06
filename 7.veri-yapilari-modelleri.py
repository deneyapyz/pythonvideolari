#Veri yapıları --> diziler
#Veri modelleri --> list, tuple, set, dictionary
#Başka kütüphanelerle birlikte farklı modeller de karşımıza çıkabilir!
"""
import array as dizi
x = dizi.array('d', [12.4, -56, 100.2, 59])

for i in range(0,4):
    print(x[i])
"""
"""
#list
liste = ["python", "java", "pascal", "c#", "basic", 123]
#tamamen boş listeyle başlarsak:
#liste = []
#print(liste)
print(liste[1:3])
print(liste[2:])
liste[2] = "c++"
liste[3] = 12.6
print(liste[:4])
liste.append("ruby")
print(liste)
liste.pop()
liste.pop()
print(liste)
"""
"""
#tuple
demet = ("python", "java", "pascal", "c#", "basic", "basic", 123)
print(demet)
print(demet[2:4])
"""
"""
#set
kume = {1, 5, 8, 9, "java", "python"}
print(kume)
kume.add(78)
print(kume)
kume.remove(9)
print(kume)
kume.add(8)
print(kume)
"""
#dictionary
sozluk = {1:'bir', 2:'iki', 3:'üç', 4:'dört', 5:'beş', 'adres':'ankara'}
#print(sozluk)
print(sozluk[4])
print(sozluk['adres'])
sozluk.pop('adres')
print(sozluk)
sozluk.popitem()
print(sozluk)
sozluk.clear()














