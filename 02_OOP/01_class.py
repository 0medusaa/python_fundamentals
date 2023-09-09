# Python'da bir obje yaratmak için "class" kullanıyoruz.
# Bu sınıflar içerisinde yaratacağımız objenin özelliklerini değişken tanımlar gibi içerisinde tanımlıyoruz.
# Bir sınıftan örneklem (instance) aldığımızda sınıf_adı() kullanıyoruz. Yani instance aldığımızda aslında sınıfın init() fonksiyonunu tetikliyoruz. init() fonksiyonu otomatik olarak knedisi tetiklenir. Bir sınıfı başlatamaya (initialize) yarar. Yani sınıfı kullanıma hazırlar. Bir diğer yeteneği ise sınıf ayağı kalkarken dışarıdan gelen değerleri sınıfın özelliklerine atar. Böylelikle sınıftna insatance alınırken obje belirli özelliklerle yaratılmış olur.

# region Example - 1
# Circle isminde bir sınıf yaratalım
# pi adında bir class attribute yaratalım
# r adında bir object attribute yaratalım
# alan ve çevre hesaplama yetenekleri fonksiyonları ekleyelim
"""
class Circle:
 	pi = 3.14

def __init__(self, radius):
 		self.r = radius

def calculate_area(self):
		return self.pi * self.r ** 2
def calculate_perimeter(self):
		return 2 * self.pi * self.r


r = float(input('Radius: '))
c1 = Circle(r)
print(c1.calculate_area())
print(c1.calculate_perimeter())


"""
# endregion

# region Example - 2
# Departmant adında bir sınıf oluşturalım
# departmant_name ve employee_count => class attribute
# name, age => object attribute
# show_info()
# show_employee_count()
# her bir çalışlan yaratıldığında person_count otomatik artsın ve show_employee_count() çalıştırılarak çalışan sayısı ekrana basılsın

class Department:
    
    department = "software developer"
    employe_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age= age
        Department.employe_count += 1
        self.show.employe_count()
    
    def show_employee_count(self):
        print(f'Total Employee: {self.employee_count}')
    def show_info(self):
        print(f'Name: {self.name}\nAge: {self.age}\nDepartment: {self.department}')
d1 = Department('Maestro', 32)
d1.show_info()
d2 = Department('Medusa', 20)
d2.department = 'ARGE'
d2.show_info()


# endregion