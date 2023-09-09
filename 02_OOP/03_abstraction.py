# Soyutlama (abstraction)
# OOP yapıları içersinde en önemlisidir.
# üst seviyeli yazılım prensiblerine (SOLİD)uymak istiyorsak ilk adım soyutlama.
# tasarım desenleri içerisinde soyutlama yoğun olarak kullanılmaktadır.
# soyutlamaya geçmeden önce öğrenmemiz gereken bir konu bulunmaktadır.


# DECORATOR
# python da kullanılan bir keyword. bir fonksiyonu bir decorator ile onun var olan yeteneği üzerine bir yetenek daha eklenir. yani adı üzerinde ilgili fonksiyonu dekore etmiş oluruz. python gibi güçlü bir dilde built-in decorator'ler bulunmaktadır. bizde custom decorator yazabiliriz.

from abc import ABC, abstractmethod

# ata entity sınıfını oluşturuyorum.

class BaseMuzikAleti:
    def __init__(self, brand, model):
        self.model= model
        self.brand= brand
class Gitar(BaseMuzikAleti):
    def __init__(self, brand, model, tel):
        super().__init__(brand, model)
        self.tel= tel
class Keman(BaseMuzikAleti):
    def __init__(self, brand, model, kasa):
        super().__init__(brand, model)
        self.kasa= kasa
class Müzisyen():
    def __init__(self, first_name, last_name):
        self.first_name= first_name
        self.last_name= last_name
        self.caldigi_enstruman = []


class BaseService(ABC):
 
    @abstractmethod
    def call_sound(self)->str: 
        pass


def hello_everyone(self):
    print("hi..")

# abstract sınıflar içerisinde static methodlar tanımlanabilinir.


class GitarService(BaseService):
    def call_sound(self)->str:
        return "gitar sesi"
    def hello_everyone(self):
        print("salve")
    
class KemanService(BaseService):
    def call_sound(self)->str:
        return "keman sesi"
# staticmethod vs instance method
@staticmethod
def harmonize():
    print("akor edildi")

def main():
    gitar_service= GitarService()
    keman_service=KemanService()

    gitar= Gitar("fender","classical gitar","kaliteli tel")
    keman = Keman("sevilla","classical","meşe")

    muzisyen = Müzisyen("burak","yılmaz")
    muzisyen.caldigi_enstruman.append(gitar) 
    muzisyen.caldigi_enstruman.append(keman)
    print(f"ad:{muzisyen.first_name}\n"
          f"soyad:{muzisyen.last_name}\n"
          f"çaldığı enstrüman adı:{muzisyen.caldigi_enstruman[0].brand}\n"
          f"çaldığı enstrüman model:{muzisyen.caldigi_enstruman[0].model}\n"
          f"çaldığı enstrüman sesi:{gitar_service.call_sound()}")
    print(f"ad:{muzisyen.first_name}\n"
          f"soyad:{muzisyen.last_name}\n"
          f"çaldığı enstrüman adı:{muzisyen.caldigi_enstruman[1].brand}\n"
          f"çaldığı enstrüman model:{muzisyen.caldigi_enstruman[1].model}\n"
          f"çaldığı enstrüman sesi:{keman_service.call_sound()}")
    KemanService.harmonize()

main()

