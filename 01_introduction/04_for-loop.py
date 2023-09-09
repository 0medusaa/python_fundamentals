# For Loop
# For Loop geçmeden önce incelememiz gereken bir kaç tane yardımcı operatör ve fonskiyon bulunmaktadır. Bunlar "in" & "not in" ayrıca range() fonksiyonudur.

# "in" operatörü bir liste içerisinde aranan ifade geçiyosa true geçmiyorsa false döner. Şunu unutmayalım string ifadelerde karakter dizileridir yani bi string ifadeye in operatörü kullanabiliriz.

# "not in" operatörü ise in operatörünün tam tersi mantıkta çalışır aranan ifade geçmiyosa true geçiyosa false döner.

# range() fonksiyonu for loop ile sıklıkla kullanılan bir yapıdır
# range(100) fonksiyonu içerisine burada olduğu gibi 100 değerini verirsek bize 0-99  arasında bir tam sayı listesi döner.
# range içerisine bir argüman verildiğinde verilen argüman "n" kabul edersek "n-1" kadar çalışır. default olarak hep sıfırdan başlayacaktır.

#for i in range(10):
#    print(i) 


# range() fonksiyonuna 2 argüman verirsek örneğin 5 ile 10. 5 ten başlayarak 10 a kadar bir sayı listesi döner
# range() fonksiyonuna 2 argüman verildiğinde birinci argüman başlangıç değerini ikinci argüman ise bitiş değerini temsil eder.

#for i in range(5,10):
#    print(i)

# region Example - 1
# Kullanıcıdan başlangıç bitiş ve adım miktalarını alalım. Bu şartlara bağlı kalarak her bir adımda ki sayının kareni alarak ekrana yazlaım

"""
baslangic = int(input("baslangic:"))
bitis = int(input("bitis:"))
adim = int(input("adim:"))
counter = 1
for i in range(baslangic, bitis, adim):
    print(f"{counter}. adımda ==> { i**2}")
    counter += 1 
"""

# endregion

# region Example - 2
# "*" sembollerini kullanarak kare sembolü yapınız
"""
edge=int(input("kenar uzunluğu giriniz:"))
for i in range(0,edge):
    for j in range(0,edge):
        print("*",end="")
    print(" ")

"""
# endregion

# region Example - 3
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

# endregion