# değişken (variable)
# yazılım dillerinde değişkenleri kutulara benzetebiliriz. nasıl ki gündelik hayatımızda kutularda eşyalar saklayabiliyorsak yazılımda değişkenler içerisinde anlık olarak değerler saklayabiliriz.

# diğer proglama dillerinde değişken tanımlarken ilk önce değişkenin tipini sonra adını sonra üzerine değer atarız.  burada şu hususa dikkat etmeyeliyiz değişkenimizi tanımlarken (declare) bir değişken tipine onu bağladık. uygulama çalıştığı sürece x değişkenin tipi "int". burada ki önemli nokta artık "x" değişkenine string bir değer atayamam.
# int x = 10
# python da değişken tanımlarken herhangi bir tip belirtmiyoruz.
# x = 10
# bir tip belirtmediğiniz için değişkenimiz anlık olarak içerisine atılan değerin tipine bürünmektedir.
# x = "maestro"

#first_name = "medusa"

# print(first_name)
# burada print() built-in  fonksiyonu aracılığı ile değişken üzerine tutulan ifadeyi ekrana yazdırdık.

#first_name = 10
# yukarıda ki satırda first_name değişkeni içerisine 10 değerini atadık. gördüğünüz gibi istediğimiz değeri değişken içerisine atayabiliyoruz. bu özellik C, C++, C#, java, php gibi programlama dillerinde bulunmamaktadır.
# print(first_name)

# region example - 1
# kullanıcıdan alınan 2 adet sayı üzerinden temel 4 işlem yapan uygulama
# kullanıcıdan input alırken python içerisinde built-in olarak bulunan input() fonksiyonunu kullanıyoruz. daha sonra kullanıcıyı doğru yönlendirmek için içerisine bir mesaj yazıyoruz. lakin şunu unutmayalım kullanıcıdan her değer aldığımızda bize gelen valunun tipi string. aritmatiksel işlem yapmak istediğimizde bize gelen değeri int değişken tipine dönüştürmemiz gerekmektedir.

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
"""
kullanıcıdan alınan kenar bilgisine göre bir karenin alanını ve çevresini hesaplayan uygulamayı yazınız.
x = int(input("lütfen bir sayı giriniz"))
# yukarı da kullanıcıdan alınan input int() fonksiyonu aracılığıyla int tipine dönüştürdük çünkü kullanıcıdan gelen değeri aritmatiksel işleme sokacağım

alan=x*x
print(alan)
cevre=x*4
print(cevre)
"""
# endregion
# region example - 3
# kullanıcıdan alınan kısa ve uzun kenar bilgilerine göre bir dikdörtgenin alanını ve çevresini hesaplayın.
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
