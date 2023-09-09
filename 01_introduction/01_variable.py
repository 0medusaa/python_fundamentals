# Değişken (variable)
# Yazılım dillerinde değişkenleri kutulara benzetebiliriz. Nasıl ki gündelik hayatımızda kutularda eşyalar saklayabiliyorsak yazılımda değişkenler içerisinde anlık olarak değerler saklayabiliriz.

# Diğer programlama dillerinde değişken tanımlarken ilk önce değişkenin tipini sonra adını sonra üzerine değer atarız.  Burada şu hususa dikkat etmeliyiz değişkenimizi tanımlarken (declare) bir değişken tipine onu bağladık. Uygulama çalıştığı sürece x değişkenin tipi "int". Burada ki önemli nokta artık "x" değişkenine string bir değer atayamam.

# int x = 10
# Python' da değişken tanımlarken herhangi bir tip belirtmiyoruz.
x = 10
# Bir tip belirtmediğiniz için değişkenimiz anlık olarak içerisine atılan değerin tipine bürünmektedir.
x = "medusa"

first_name = "medusa"
# Burada print() built-in  fonksiyonu aracılığı ile değişken üzerine tutulan ifadeyi ekrana yazdırdık.

first_name = 10
# Yukarıda ki satırda first_name değişkeni içerisine 10 değerini atadık. Gördüğünüz gibi istediğimiz değeri değişken içerisine atayabiliyoruz. Bu özellik C, C++, C#, java, php gibi programlama dillerinde bulunmamaktadır.
print(first_name)


# region example - 1
# Kullanıcıdan alınan 2 adet sayı üzerinden temel 4 işlem yapan uygulama istiyoruz.
# Kullanıcıdan input alırken python içerisinde built-in olarak bulunan input() fonksiyonunu kullanıyoruz. daha sonra kullanıcıyı doğru yönlendirmek için içerisine bir mesaj yazıyoruz. Lakin şunu unutmayalım kullanıcıdan her değer aldığımızda bize gelen valuenun tipi string. aritmatiksel işlem yapmak istediğimizde bize gelen değeri int değişken tipine dönüştürmemiz gerekmektedir.

"""
    sayi_1 = int(input("lütfen bir sayı giriniz:"))
    sayi_2 = int(input("lütfen bir sayı giriniz:"))

    toplam = sayi_1 + sayi_2
    print(f' sonuc: {toplam}')

    cıkarma = sayi_1 - sayi_2
    print (f'çikarma işleminin sonucu :{cıkarma}')

    carpma = sayi_1 * sayi_2
    print('{} x {} = {}' .format(sayi_1,sayi_2, carpma))

    bölme = sayi_1/sayi_2
    print(f'{sayi_1}/  {sayi_2} = {bölme}')

"""
# endregion

# region example - 2
# Kullanıcıdan alınan kenar bilgisine göre bir karenin alanını ve çevresini hesaplayan uygulamayı yazınız.
"""
x = int(input("lütfen bir sayı giriniz"))
# yukarı da kullanıcıdan alınan input int() fonksiyonu aracılığıyla int tipine dönüştürdük çünkü kullanıcıdan gelen değeri aritmatiksel işleme sokacağız.

alan=x*x
print(alan)
cevre=x*4
print(cevre)
"""
# endregion

# region example - 3
# Kullanıcıdan alınan kısa ve uzun kenar bilgilerine göre bir dikdörtgenin alanını ve çevresini hesaplayın.
"""
kenar_1=int(input("lütfen sayı giriniz"))
kenar_2=int(input("lütfen sayı giriniz"))
alan=kenar_1*kenar_2
print(alan)

cevre=kenar_1*2 + kenar_2*2
print(cevre)
"""

# endregion

# region example - 4
# Üçgenin alanını hesaplayalım
"""
taban= float(input("lütfen bir sayı giriniz"))
yükseklik= float(input("lütfen bir sayı giriniz"))

alan= taban*yükseklik/2
print(alan)
"""


# endregion
