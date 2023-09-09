# Tuple (Demetler)
# List objesi ile benzer bir mantığı vardır. Lakin listelere uyguladığımız gömülü fonskiyonlara(built-in functions) sahip değildir. Bunun yanında index mantıkları aynıdır. Hem listelerde hem de tuple'larda dilimleme (slicing) işlemi yapılabilir. demetler list objeleri gibi RAM'de tutulmaktadır. yani uygulama run time'da iken üzerine eklediğimiz değerler tutulur, uygulama kapatıldığında uçar giderler.

# region Example
my_family = [
    ("berk karadaş", 33, "maestro"),
    ("berk bayındır", 31, "beta"),
    ("aşkın mert şalcıoğlu",18," vio")
]

for x,y,z in my_family:
    print(f"full name: {x}\nAge: {y}\nUser Name: {z}")

# endregion