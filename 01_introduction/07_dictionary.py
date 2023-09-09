# Dictionary (sözlük)
# Sözlük objesi, list, tuple gibi geçici olarak verileri depolayabildiğimiz başka bir yapıdır. 
# Sözlükler "key" & "value" mantığında çalışırlar.
# Anahtarlar herhangi bir değere erişmek için kullanılırlar.



release_year_movies = {
    "fight club": 1999,
    "matrix": 1999,
    "ınterstaller": 2014,
    "inception": 2010,
    "dune": 2021,
}

# Herhangi bir filmin anahtarını çağırarak değerini ekrana yazınız
# yol I
print(f"interstaller release year:{release_year_movies.get('interstaller')}")

# yol II
print(f"interstaller release year:{release_year_movies['ınterstaller']}")


# sözlüğün bütün anahtarlarını dökün 
print(f'movie list: {type(release_year_movies.keys())}')
for i in release_year_movies.keys():
    print(i)

# sözlüğün tüm değerlerini dökün
print([i for i in release_year_movies.values()])

from pprint import pprint
pprint({name: year for name, year in release_year_movies.items()})
