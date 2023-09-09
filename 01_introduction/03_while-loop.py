# While Loop
# While döngülerinde belirttiğimiz bir koşul doğru olduğu sürece while bloğu içerisinde tanımladığımız kod satırlarını tekrarlatabiliriz.
# region Example - 1
# 0-100 arasında ki sayıları ekrana yazdıralım
"""
sayac = 0
while sayac <= 100:
    print(sayac) 
    sayac = sayac + 1
"""
# endregion

# region Example - 2
# 1-101 arasındaki çif ve tek sayıların miktarını ekrana yazalım
"""
sayac = 1  # sayac 1 çünkü soruda 1 ile 101 arasında ki sayılar istenmiş sayaç bu aralıkta ki sayıları tek tek ziyaret edecek
     # Aşağıda ki iki değişken her çift yada tek sayı yakaladığımda arttırılacak.
cift_sayilar = 0
tek_sayilar = 0
while sayac < 101:
 	if sayac % 2 == 0:
 		cift_sayilar += 1
else:
 		tek_sayilar += 1

sayac += 1  # sayac = sayac + 1

print(f'1 - 101 arasında, {cift_sayilar} kadar çift sayı, {tek_sayilar} kadar tek sayı bulunmaktadır.')
"""

# endregion

# region Example - 3
# Kullanıcıdan bir işlem türü alalım ("+","-" vs)  ve 2 adet sayı üzerinden kullanıcının istediği işlemi gerçekleştirelim. Kullanıcı klavyeden e harfi gönderirse uygulamayı durduralım. kullanıcı isterse sonsuza kadar işlem yapabilsin.
"""
process_type_list=["+","-","/","e"]

while True:
    process = input("işlem işareti giriniz")

    if process in process_type_list:
        # in operatörü ile bir liste içersinde item varsa true yoksa false döner. yani burada kullanıcının girdiği işlem bizim işlem türü listemizde varsa true yoksa false dönücek.

        if process =="e":
            print("uygulama kapatılıyor")
            break
        else:
            sayi_1=int(input("sayı giriniz"))
            sayi_2=int(input("sayı giriniz"))

            if process=="+":
                print(f'sonuc:{sayi_1+sayi_2}')

            elif process=="-":
                print(f'sonuc:{sayi_1 - sayi_2}')
            elif process=="/":
                print(f'sonuc:{sayi_1 / sayi_2}')
    else:
                print(" lütfen doğru bi işlem giriniz")
                
"""


# endregion

