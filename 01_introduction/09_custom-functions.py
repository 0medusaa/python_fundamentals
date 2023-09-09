# custom functions
# Bu zamana kadar python içerisinde built-in olarak bulunan fonksiyonları gördük. örneğin print(), range(), split(), randint() vb. fonksiyonlar onların üzerilerine atanmış olarak işleri bıkmadan usanmadan yerine getirirler. Bazen yaptıkları işlemler doğrultusunda değer dönerler bazende dönmezler. Aldıkları argümanlara göre üzerlerine yüklenen işlerin değişik versiyonlarını yerine getirirler. Örneğin range() fonksiyonu aldığı argümanlara göre değişik işlemler yapmaktaydı.

# fonksiyon tanımlarken
# def fonksiyon_name():
#(tab)     yapılacak işlem kodları
# fonksiyon bir kez tanımlanır

# fonksiyon_name() artık istediğimiz yerde istediğimiz kadar fonksiyonu çağırarak kullanabiliriz.

# region Example - 1
# kullanıcıdan alınan sayı çift mi tek mi olduğunu söyleyen fonksiyonu yazınız.

"""
def cift_tek(sayi:int)->None:

    if sayi%2==0:
        print("sayı çift")
    else:
        print("sayı tek")
number= int(input("sayi:"))
cift_tek(number)

"""

# endregion

# region Example - 2
# lşst içerisinde ki çift sayıların 2 ile çarparak, tek sayıları 3 ile çarparak sonucunu lst_1 içerisine ekleyelim.
"""
lst = [12,11,19,2,99]
lst_1 = []

def tek_cift_mi(sayi:int) ->str:
    if sayi % 2 == 0:
        return 'cift'
    else:
        return 'tek'
    
def append_list(result:str, counter:int)->None:
    if result == 'cift':
        lst_1.append(counter*2)
    else:
        lst_1.append(counter*3)
    print(lst_1)

    
def main():
    for i in lst:
        result = tek_cift_mi(i)
        append_list(result, i)

main()
"""
# endregion

