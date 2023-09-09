# API'lerden hızlıca veri talebinde bulunmak için python içerisinde bulunan "request" modülünden faydalanacağız. 
# API'leri günlük hayatımızda yoğun olarak kullanmaktayız. web sitelerinde hava durumu genellikle OpenWeatherAPI gelen veri ile oluşturulur. facebook, google apileri kullanılarak 3rd uygulamalar geliştirebiliyoruz. Yine apileri kullanarak basit oyunlar tasarlayabiliriz.
# Günümüzde çok popüler olan ChatGPT'de bir apidir. Sizlerden gelen talebi backend iletir.

# B çalışmada free NewsAPI'den tesla ile alakalı makaleleri çekeceğiz. Bu işlem için "https://newsapi.org/" sitesine login olup bir api key aldık. bu "key" bize veri cekme olanağı verecektir.

from pprint import pprint
# requests modülü python core dosyaları arasında bulunmamaktadır. bu yüzden bu modülü yüklememiz gerekmektedir.
# bunun için "terminal" ekranına gelene "pip install requests" diyebilir ya da ilgili modülü yüklediğimiz  satıra gelip yüklem işlemini GUİ üzerinden yerine getirebiliriz
# python da harici bir modül ile ilgili bilgi almak istersek bakacağımız site ise "https://pypi.org/"
from requests import get

# requests modülünü kullanarak ilgili api'yi talep (requests) atacağız. bu talep sonucunda bize bir cevap (response) döner.
 
response = get("https://newsapi.org/v2/everything?q=tesla&from=2023-04-20&sortBy=publishedAt&apiKey=f6c08a0fcd9e402c9e84b44e80bcbf70")

# günümüzde internetin çalışma mantığı çok basittir. kullanıcılar bir web sitesine talepte( requests) ve web siteside bir cevap (response) döner.bu mantığa HTTP Protokolü denir. bu protokolün mantığına göre yukarıdaki  api'ye http requests attık.

tesla_data = response.json()
# Json(javascript object notation), değişik platformlarda koşan yani çalışan uygulamaların kendi aralarında veri transferi yaparken kullandıkları bir notasyondur.

pprint(tesla_data)
author = tesla_data.get("articles")[1].get("author")
title = tesla_data.get("articles")[1].get("title")
published_at = tesla_data.get("articles")[1].get("publishedAt")

print(f"author:{author}")
print(f"title:{title}")
print(f"published date:{published_at}")


# kullanıcıdan yazar ismi alınacak, alınan bu yazar ismine göre ham data search edilecek
# ilgili yazarların makalesi ekrana basılacak.
author_name= input("author name:")
for article in tesla_data.get("articles"):
    if article.get("author") == author_name:
        pprint(article)



