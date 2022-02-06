"""
toplam = 0
for i in range(101):
    toplam += i
# 0 + 0 + 1 + 2 + 3 + 4 + 5 + 6
print(toplam)
"""
"""
for i in range(5):
    print("python")
"""
"""
for i in range(1, 11):
    print(i)
"""
"""
print("0 ile 10 arası çift sayılar:")
for i in range(0, 11, 2):
    print(i)

print("1 ile 10 arası tek sayılar:")
for i in range(1, 11, 2):
    print(i)
    
print("0'dan 100'e kadar 10'a bölünebilen sayılar:")
for i in range(0, 101, 10):
    print(i)
"""
"""
print("0'dan 100'e kadar 3'e veya 10'a bölünebilen sayılar:")
for i in range(101):
    if (i % 10 == 0):
        print("10'a bölünen:",i)
    elif (i % 3 == 0):
        print("3'e bölünen:",i)
"""
"""
#Klavyeden girilen [x,y] toplamı...
x = int(input("Başlangıç değerini giriniz:"))
y = int(input("Bitiş değerini giriniz:"))
toplam = 0
for i in range(x,y+1):
    toplam+=i

print(toplam)
"""
"""
for i in range(10,0,-1):
    print(i)
print("Tersine kelimesi kullanımı:")
for i in reversed(range(10)):
    print(i)
"""
"""
kelime = "python"
for harf in kelime:
    print(harf)

sayilar = "123456789"
for a in sayilar:
    print(int(a)*2)
"""
#break, continue, pass
"""
for x in range(11):
    if (x % 2 == 1):
        #Bu adımı atlıyoruz...
        continue
    else:
        print(x)
"""
"""
for x in range(11):
    if (x == 6):
        #Burada döngüyü kırıyoruz...
        break
    else:
        print(x)
print("Kırılmış döngüden sonraki ilk komut...")
"""
"""
for x in range(11):
    if (x % 2 == 1):
        #Bu adımı atlıyoruz...
        #continue
        #Burayı pas geçiyoruz...
        pass
    else:
        print(x)
    print(x,"değeri için çalıştı...")
"""

#iç içe for döngüleri
"""
for i in range(11):
    for j in range(5):
        print(i,"üssü",j,"=",i**j)
"""
"""
for i in range(11):
    if (i % 2 == 0):
        for j in range(i):
            print(j)
"""

for i in range(6):
    for j in range(6):
        for k in range(6):
            print(i,j,k)
