# region documantation
# karar mekanizmaları (if - elif - else)
# uygulama içerisinde karar mekanizmaları ile belirli bir şart tutması ya da tutmaması durumuna göre farklı kod bloklarının çalışmasını temin eden yapıdır.
# if kullanımı
#if şart_cümlesi:
#  kod_blogu:
# else: ==> else şart cümlesi içermez çünkü if bloğunda verilen şart tutmama durumunu kontrol eder.
#    kod_bloğu

# endregion
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
# kullanıcıdan alınan sayı çift mi tek mi?
"""
sayi=int(input("lütfen bir sayı giriniz:"))

if sayi % 2==0:
    print("girilen sayı çifttir")
else:
    print("girilen sayı tektir")

"""

# endregion
# region example - 3
# kullanıcıdan alınan sayı pozitif mi negatif?
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
# kullanıcıdan mevsim bilgisini alalım alınan mevsim bilgisine göre ayları ekrana yazdıralım
"""
mevsim = input("lütfen bir mevsim giriniz").lower() 
#burada kullanılan lower() python içerisinde built-in olarak bulunan bu fonksiyonu ile kullanıcıdan alınan input küçük harfe dönüştürülür
mesaj= ""
if mevsim== 'kis':
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
# linear bir doğrunun reel köklerini hesaplayalım.
"""from math  import sqrt
a= int(input("birinci kat sayı"))
b= int(input("ikinci kat sayı"))
c= int(input("üçüncü kat sayı"))

delta = b**2-4*a*c
if delta> 0:
    x1 = -b - sqrt(delta)/2*a
    x2= - b + sqrt(delta)/2*a 
    print(f'2 real kök bulunmaktadır./n')
elif delta==0:
    x1 = -b - sqrt(delta)/2*a
    print(f'1 real kök bulunmaktadır./n')

    
else:
    print("reel kök bulunmamaktadır.") 

"""
# endregion
# region uyarı
# uyarı: python da aritmatiksel işlemler için kullanılan bir modül bulunmaktadır. bu modülün adı "math". karekök işlemi için bu modül içersinde bulunan sqrt() fonksiyonundan faydalanacağız bu modülden faydalanabilmek için çalışma dosyamıza import etmemiz gerekir.!
# endregion
# region example - 6
