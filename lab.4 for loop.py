# for loop
# for loop geçmeden önce incelememiz gereken bir kaç tane yardımcı operatör ve fonskiyon bulunmaktadır. bunlar "in" & "not in" ayrıca range() fonksiyonudur.

# in operatörü bir liste içerisinde aranan ifade geçiyosa true geçmiyorsa false döner. şunu unutmayalım string ifadelerde karakter dizileridir yani bi string ifadeye in operatörü kullanabiliriz.

# not in operatörü ise in operatörünün tam tersi mantıkta çalışır aranan ifade geçmiyosa true geçiyosa false döner.

# name= "maestro"

"""
#print("b"in name)
print("m" in name)
print("M" in name)
"""
"""
import random
"""
"""
print("M" not in name)
"""

# range() fonksiyonu for loop ile sıklıkla kullanılan bir yapıdır
# range(100) fonksiyonu içerisine burada olduğu gibi 100 değerini verirsek bize 0-99  arasında bir tam sayı listesi döner.

# unutmayın range içerisine bir argüman verildiğinde verilen argüman "n" kabul edersek "n-1" kadar çalışır. default olarak hep sıfırdan başlayacaktır.

 #for i in range(10):
# print(i) # burada print() fonksiyonu değerleri alt alta yazmaktadır. bunu yan yana yazdırmanın yolunu bulun

# range() fonksiyonuna 2 argüman verirsek örneğin 5 ile 10. 5 ten başlayarak 10 a kadar bir sayı listesi döner
# range() fonksiyonuna 2 argüman verildiğinde birinci argüman başlangıç değerini ikinci argüman ise bitiş değerini temsil eder.

#for i in range(5,10):
 #   print(i)

# range() 3 argüman verirsek.1. argüman başlangıç, ikinci argüman bitiş üçüncü argüman ise adım miktarını temsil eder.

#for i in range(1,21,2):
 #   print(i)
# region example - 5
# 1-100 arasındaki çift ve tek sayıların toplamını
# ciftlerin_toplami = 0
# teklerin_toplami = 0
# for i in range(1, 101):  # while loop olduğu gibi adım miktarını biz arttırmıyoruz aksini söylemediğimiz sürece 1 olarak yani dafult bir kabul edip çalışır
# 	if i % 2 == 0:
# 		ciftlerin_toplami += i
# 	else:
# 		teklerin_toplami += i
#
# print(f'Ciftlerin Toplamı: {ciftlerin_toplami}\nTeklerin Toplamı: {teklerin_toplami}')

# endregion

# Kullanıcıdan başlangıç bitiş ve adım miktalarını alalım. BU şartlara bağlı kalarak her bir adımda ki sayının kareni alarak ekrana yazlaım
# çıktıyı şu formatta istiyorum 1. adımda ki sonuç: 2
"""
baslangic = int(input("baslangic:"))
bitis = int(input("bitis:"))
adim = int(input("adim:"))
counter = 1
for i in range(baslangic, bitis, adim):
    print(f"{counter}. adımda ==> { i**2}")
    counter += 1 
"""
# kullanıcıdan alınan sayı asal mı değil mi?
"""
sayi = int(input("sayı giriniz:"))
if sayi <=0:
    print("sıfır ve negatif sayılar asal değildir..")
else:
    is_prime = True
    if sayi ==1:
        is_prime = False

    for i in range(2, sayi):
        if sayi % i == 0 :
            is_prime = False
            break

    if is_prime: # burada is_prime değişkeni üzerinde true varsa if bloğunda tetiklenicek
        print(f"{sayi}asaldır")

    else:
        print(f"{sayi}asal değildir")
"""
# 0-1000 arasındaki sayıları 10'ar 10'ar toplayalım. her bir adımda ki toplam kullanıcıya gösterelim
"""
counter = 1
toplam = 0
for i in range(0,1001,10):
    toplam += i
    print(f"{counter}. adımda toplama sonucu: {toplam}")
    counter+=1

"""
# iç içe for loop
"""
for i in range(0,11):
    for j in range(0,11):
        print(f"{i}x {j}= {i*j}")
    print("=========")
"""
# "*" sembollerini kullanarak kare sembolü yapınız
"""
edge=int(input("kenar uzunluğu giriniz:"))
for i in range(0,edge):
    for j in range(0,edge):
        print("*",end="")
    print(" ")

"""
# içi boş bir listeye rakamları ekleyelim
"""
sayilar= []
for i in range(0,10):
    sayilar.append(i)
print(sayilar)
"""
# boş bir listenin içerisine 0 -100 arasında olcak şekilde rastgele 10 adet sayı ile doldurun
"""
from random import randint
lst=[]
for i in range(0,10):
    random.number=randint(0,101)
    lst.append(random_number)
print(lst)
"""
# 0,100 arasında olacak şekilde rastgele 10 adet sayı üretin, üretilen bu sayılardan 3 tam bölünenlerin karesi bir listeye doldurun.
"""
from random import randint
for i in range(0,10):
    random.number=randint(0,100)
    if random_number % 3 == 0:
        print(random_number)
        sayilar.append(random_number**2)

"""
# kullanıcıdan bir söz öbeği alıyoruz
# örneğin merhabalar ben medusa
# yukarıda ki  örnek söz öbeğinde ki her bir harfi bir listeye ekleyelim
# yol I
# söz öbeği içerisinde adım adım dolaşarak
# yol II
# söz öbeğinde ki her bir harfi döngüye itarete ederek yaptın
# yol I
"""

soz_obeği = input("Lütfen bir söz öbeği giriniz: ")

harfler = [] 

for harf in soz_obeği:
    harfler.append(harf)

print(harfler)
"""
"""
word= input("please type something:")
lst=[]
print(len(word))
for i in range(0, len(word)):
    if word[i] != " ":
        lst.append(word[i])
"""
# yol II
"""
soz_obeği = input("Lütfen bir söz öbeği giriniz: ")

harfler = [harf for harf in soz_obeği]

print(harfler)
"""
"""
word= input("please type something:")
lst=[]
for character in word:
    if character !=" ":
        lst.append(character)
print(lst)

"""
