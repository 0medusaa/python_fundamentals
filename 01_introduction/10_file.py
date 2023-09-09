# file I/10
# Dosya açma, kapama, var olan dosya üzerine yeni bilgiler yazma silme yani dosya üzerinden CRUD işlemlerini yapmak için python içerisine bulunan File I/10 modülünü kullanacağız.

# Dosya açma
"""
file = open(file="new_file.text", mode="a",encoding="utf-8")

"""

# Dosya içerisinde yazan her şeyi okumak istediğimizde "mode" argümanına "r" yani readable olarak dosyamızı aç diyoruz.
"""
file = open(file="new_file.text", mode="r",encoding="utf-8")
sentences= file.readlines()
for sentence in sentences:
    print(sentence)
"""


#x = 5 / 0
# yukarıdaki kod çalıştığında
#Traceback (most recent call last):
#  File "c:\Users\Pc\Desktop\python\lab\lab13.py", line 59, in <module>
#    x = 5 / 0
#        ~~^~~
#ZeroDivisionError: division by zero
"""
try:
    x = 5 / 0
    print(x)
except ZeroDivisionError as ex:
        print(err.__doc__)
"""
"""
try:

    lst=[12,34,56]
    print(lst[10])
except: # burada spesifik bir exception modülü belirtmedik. bütün exception modülüne burada kontrol ederek hangi exception geldiyse ona göre hareket edicek.
    print(f"listenin eleman sayısı:{lst.__len__()} ")
"""
from random import choice
exceptions = [ValueError, TypeError, IndexError, None]
try:
    random_err= choice(exceptions)
    print(f"random exceptions is {random_err} and it type is {type(random_err)}")

    if random_err: # random_err değişkeni dolu ise if bloğu çalışacak zaten boş olma olasılığı yok.
        raise random_err("an error happend...") # burada raise anahtar sözcüğüyle exception biz kendi elimizle tetiklemiş olduk. burada bir exception raise olduğu için uygulama durucak ve "except" bloğuna inecek
except ValueError as err:
    print(f"caught a value error. \n{err.__doc__}")
except TypeError as err:
    print(f"type error happend. \n{err.__doc__}")
except IndexError as err:
    print(f"index error happend. \n{err.__doc__}")
else: 
    # herhangi exception tetiklendmez ise else bloğu devreye girer.
    print("if there is no exception when this code call")
finally:
    # finally bloğu try bloğu başarılı olsada çalışır, exception dediğimizde de çalışır her durum ve koşul altında çalışır
    print(" no matter what this block can be call...")
