# List
# Uygulama içerisinde anlık olarak bizim için değer tutan bir yapıdır. birden fazla tipte farklı tipte değer tutabilir. Listeler RAM üzerinde tutulduğu için uygulama çalıştığı sürece üzerine yeni eklenen değerleri saklarlar. Yani uygulama kapatıldığında ilk yaratıldığı hale döner.

# append() ==> fonksiyonu ile listenin sonuna yeni bir eleman ekletiriz
# insert() fonksiyonu listenin herhangi bir index değerine eleman ekleme işlemini yerine getirir.
# remove() ==> listeden silinmesini istediğimiz item'in değerini kendisine vererek silme işlemini gerçekleştiriyoruz.
# clear() => fonksiyonu listenin hepsini siler.
# pop() => verilen index değerinde ki elemanı siler.
# extend() => iki farklı listeyi bileştirmeye yarar.

# region Example - 1
# 2 farklı liste içerisine random olarak 10 adet sayı ile dolduralım.sayılar 0-100 arasında üretilsin, ilk adımda doldurulan bu iki listenin karşılıklı gelen index değerleri toplanarak 3. bir listeye eklensin
"""
from random import randint
lst_1=[]
lst_2=[]
lst_3=[]
for i in range(10):
    lst_1.insert(i, randint(0,101))
    lst_2.insert(i, randint(0,101))

    lst_3.insert(i, lst_1[i]+lst_2[i])

    print(f" {lst_1[i]}+ {lst_2[i]}={lst_3[i]}")

print(lst_3)
"""

# endregion

# region Example - 2
# kullanıcıdan alınan söz öbeğinde ki sesli harfleri bir listeye dolduralım ,sesli harfleri tekrar etmesin,söz öbeğindeki rakamları bir listeye doldurun
"""
sesli_harfler=["a","e","ı","i","o","ö","u","ü"]
yakalanan_sesli_harf=[]
yakalanan_sayilar=[]
cumle=input("lütfen bir cümle giriniz")
bosluk_sayisi=0

for karakter in cumle:
    if karakter in sesli_harfler:
        if karakter not in yakalanan_sesli_harf:
            yakalanan_sesli_harf.append(karakter)
    elif karakter == " ":
        bosluk_sayisi += 1
    elif karakter.isdigit():
        yakalanan_sayilar.append(karakter)
print(yakalanan_sesli_harf)
print(yakalanan_sayilar)
print(f"yakalanan bosluk sayisi: {bosluk_sayisi}")

"""
# endregion

# region Example - 3
# 0-100 arasında 3 tam bölünen sayıların karesini listeye dolduralım
"""
print([i * i for i in range(100) if i % 3 == 0])
"""
# endregion