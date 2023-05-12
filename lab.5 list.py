# list
# uygulama içerisinde anlık olarak bizim için değer tutan bir yapıdır. birden fazla tipte farklı tipte değer tutabilir. listeler RAM üzerinde tutulduğu için uygulama çalıştığı sürece üzerine yeni eklenen değerleri saklarlar. yani uygulama kapatıldığında ilk yaratıldığı hale döner.
# örneğin bir futbol takımları listem olsun
# futbol_takimlari = ["besiktas","galatasaray","adanademir spor"]
# uygulama çalıştırıldığında bu liste tam olarak yukarıda ki yapıda RAM'in Heap alanına çıkartılır.
# uygulama run time'da yani çalışıyor. aşağıdaki kod çalıştığını var sayalım
# futbol_takimlari.append("trabzon")
# artık listem 4 elemanlı. lakin uygulama shutdown edildiğinde ilk yaratıldığı hale geri dönecektir. çünkü listeler RAM'de saklanır.
# listeler index mantığı ile çalışır yani listemin birinci elemanına erişmek isterse
# futbol_takimlari[0] demem gerekmektedir.
# garcabe collector ve ram arastır.
# top_boxers = ["mike tyson"," muhammed ali","lenox lewis","evander holyfield","rocky marciano" ]
# append() ==> fonksiyonu ile listenin sonuna yeni bir eleman ekletiriz
# top_boxers.append("george forman")
# print(top_boxers")
# insert() fonksiyonu listenin herhangi bir index değerine eleman ekleme işlemini yerine getirir.
# aldığı ilk parametre index değerini
# ikinci parametre ise value temsil eder
# top_boxers.insert(3, "floyd mayweater")
# print(top_boxers)
# remove() ==> listeden silinmesini istediğimiz item'in değerini kendisine vererek silme işlemini gerçekleştiriyoruz
# top_boxers.remove("lenox lewis")
# clear() => fonksiyonu listenin alayını siler
# top_boxers.clear()
# pop() => verilen index değerinde ki elemanı siler
# top_boxers.pop(4)
# extend() => iki farklı listeyi bileştirmeye yarar.
# current_boxers = ["tyson fury", "deantony wilder", "antony jasua"]
# top_boxers.extend(current_boxers)
"""
movies=["fight clup","matrix"," interstallar", "inception"]

for movie in movies:
    print(movie)

for i in range(0,len(movies)):
    print(movies[i])
"""
# 2 farklı liste içerisine random olarak 10 adet sayı ile dolduralım
# sayılar 0-100 arasında üretilsin
# ilk adımda doldurulan bu iki listenin karşılıklı gelen index değerleri toplanarak 3. bir listeye eklensin
# lütfen index mantığıyla çözelim
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

# kullanıcıdan alınan söz öbeğinde ki sesli harfleri bir listeye dolduralım
# sesli harfleri tekrar etmesin
# boşlukları sayın
# söz öbeğindeki rakamları bir listeye doldurun
"""
# tekrar kendin çöz
soz_obeği = input("Lütfen bir söz öbeği giriniz: ")
harfler= []
sesli_harfler=["A","E","I","İ", "O","Ö","U","Ü"]
for harf in soz_obeği:
    if soz_obegi == sesli_harfler:
        print(harf)
print(sesli_harfler)
"""
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
# list comprehansion
# rakamları bir listeye ekleme
"""
sayilar= []
for i in range(10):
    sayilar.append(i)
print(sayilar)

print([i for i in range(10)])
"""
# rakamların karesini listeye dolduralım
"""
print([i* i for i in range(10)])

"""
# 0-100 arasında 3 tam bölünen sayıların karesini listeye dolduralım
"""
