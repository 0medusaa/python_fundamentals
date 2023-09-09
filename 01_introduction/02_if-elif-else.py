# Documantation 
# Karar Mekanizmaları (if - elif - else)
# Uygulama içerisinde karar mekanizmaları ile belirli bir şart tutması ya da tutmaması durumuna göre farklı kod bloklarının çalışmasını temin eden yapıdır.
"""
if kullanımı
 if şart_cümlesi:
  kod_blogu:
 else: ==> else şart cümlesi içermez çünkü if bloğunda verilen şart tutmama durumunu kontrol eder.
  kod_bloğu

"""

# region example - 1
"""
sayi_1 = int(input("sayı girin:"))
sayi_2 = int(input("sayı girin:"))

if sayi_1> sayi_2:
    print(f'{sayi_1}büyüktür')
else:
    print(f'{sayi_2}büyütür')
"""

# endregion

# region example - 2
# Kullanıcıdan alınan sayı çift mi tek mi?
"""
sayi=int(input("lütfen bir sayı giriniz:"))

if sayi % 2==0:
    print("girilen sayı çifttir")
else:
    print("girilen sayı tektir")

"""

# endregion

# region example - 3
# Kullanıcıdan alınan sayı pozitif mi negatif?
"""
sayi= float(input("bir sayı girin:"))
if sayi>0:
    print("girdiğiniz sayı pozitif")
elif sayi<0:
    print("girdiğiniz sayı negatif")
else:
    print("girdiğiniz değer sıfır veya bir sayı değil")  
"""
  
# endregion

# region example - 4
# Kullanıcıdan mevsim bilgisini alalım alınan mevsim bilgisine göre ayları ekrana yazdıralım
"""
mevsim = input("lütfen bir mevsim giriniz").lower() 
# Burada kullanılan lower() python içerisinde built-in olarak bulunan bu fonksiyonu ile kullanıcıdan alınan input küçük harfe dönüştürülür
mesaj= ""
if mevsim== "kış":
    mesaj="aralık- ocak- subat"
elif mevsim=="ilkbahar":
    mesaj="mart nisan mayıs"
elif mevsim=="yaz":
    mesaj="haziran temmuz ağustos"
elif mevsim=="sonbahar":
    mesaj="eylül ekim kasım"
else:
    mesaj= "böyle bir mevsim yok"

    print(mesaj)
"""
# endregion

# region example - 5
# Kullanıcıdan alınan vize final ödev notuna göre ortalama hesaplayalım ve harf notunu ekrana yazdıralım.
"""
vize=float(input("vize:"))
final=float(input("final:"))
odev=float(input("odev:"))

ort= vize * 0.3 + final * 0.6 + odev * 0.1

if 90<= ort <=100:
    print("AA")

elif 85<=ort<=89:
    print("ba")

elif 80<= ort <= 84:
    print("bb")

elif 75<=ort<=79:
    print("cb")

elif 70<=ort<=74:
    print("cd")

elif 65<=ort<=69:
    print("cd")

elif 60<=ort<=64:
    print("dd")

elif 55<=ort<=59:
    print("dc")

elif 50<=ort<=54:
    print("fd")

else:
    print("ff")
"""


# endregion
